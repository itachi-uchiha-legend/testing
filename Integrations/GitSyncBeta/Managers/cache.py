import collections
import copy
import json
from collections.abc import Iterable, Iterator, MutableMapping, MutableSequence, Set
from typing import Generic, Protocol, TypeAlias, TypeVar

import SiemplifyBase
import SiemplifyUtils
from SiemplifyAction import SiemplifyAction
from SiemplifyJob import SiemplifyJob


_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_Index: TypeAlias = int
_Record: TypeAlias = MutableMapping[_KT, _VT]
_Cache: TypeAlias = MutableSequence[_Record]
_KeyToIndex: TypeAlias = MutableMapping[_KT, _Index]
_CacheInitData = collections.namedtuple("_CacheInitData", ["cache", "largest_index"])
JsonStr: TypeAlias = str

CONTEXT_MOD_TIME_KEY: str = "name_to_modification_time_mapping_{0}"
ROW_PADDING_LENGTH: int = 40
ACTION_GLOBAL_CONTENT_TYPE: int = 0
GLOBAL_CONTEXT_IDENTIFIER: str = "GLOBAL"


class Context(Protocol):
    """Context protocol to have a standard signature across different SDK
    implementations.
    """

    def set_context(self, key: str, value: str | JsonStr) -> None:
        """Set context in the database. It must be a string."""

    def get_context(self, key: str) -> str | JsonStr | None:
        """Get context from the database. The content will be a string"""


def get_context_factory(_s: SiemplifyAction | SiemplifyJob) -> Context:
    """Factory to get a context object depending on SDK object type."""
    if isinstance(_s, SiemplifyJob):
        return SiemplifyJobContext(_s)

    if isinstance(_s, SiemplifyAction):
        return SiemplifyActionContext(_s)

    raise RuntimeError(f"Unsupported SDK object {_s} of type {type(_s)}")


class SiemplifyJobContext(Context):
    """Context implementations for SiemplifyJob."""

    def __init__(self, _s: SiemplifyJob, /) -> None:
        self._s: SiemplifyJob = _s

    def get_context(self, key: str) -> str | JsonStr | None:
        return self._s.get_scoped_job_context_property(key)

    def set_context(self, key: str, value: str | JsonStr) -> None:
        self._s.set_scoped_job_context_property(key, value)


class SiemplifyActionContext(Context):
    """Context implementations for SiemplifyAction."""

    def __init__(self, _s: SiemplifyAction, /) -> None:
        self._s: SiemplifyAction = _s

    def get_context(self, key: str) -> str | JsonStr | None:
        return self._s.get_context_property(
            context_type=ACTION_GLOBAL_CONTENT_TYPE,
            identifier=GLOBAL_CONTEXT_IDENTIFIER,
            property_key=key,
        )

    def set_context(self, key: str, value: str | JsonStr) -> None:
        self._s.set_context_property(
            context_type=ACTION_GLOBAL_CONTENT_TYPE,
            identifier=GLOBAL_CONTEXT_IDENTIFIER,
            property_key=key,
            property_value=value,
        )


class Cache(MutableMapping[_KT, _VT], Generic[_KT, _VT]):
    """Class that handles cache like a dict while abstracting DB handling,
    data distribution and rows managing from the user.
    """

    def __init__(self, context_handler: Context) -> None:
        self._context: Context = context_handler
        self._no_saved_context: bool = self._get_no_saved_context()
        cache_init_data: _CacheInitData = self._get_cache_init_data()
        self._largest_row_index: _Index = cache_init_data.largest_index
        self._cache: _Cache = cache_init_data.cache
        self._key_to_row_index: _KeyToIndex[_KT] = self._init_key_to_row_map()
        self._new_cache: _Record[_KT, _VT] = {}

    def _get_no_saved_context(self) -> bool:
        return self._get_scoped_job_context_property(0) is None

    def _get_cache_init_data(self) -> _CacheInitData:
        if self._no_saved_context:
            return _CacheInitData(cache=[{}], largest_index=0)

        i: _Index = 0
        cache: _Cache = []
        context: JsonStr | None = self._get_scoped_job_context_property(i)
        while context is not None:
            cache.append(_load_record(context))
            i += 1
            context = self._get_scoped_job_context_property(i)

        return _CacheInitData(cache=cache, largest_index=i - 1)

    def _init_key_to_row_map(self) -> _KeyToIndex[_KT]:
        results: _KeyToIndex[_KT] = {}
        for i, record in enumerate(self._cache):
            for key in record:
                results[key] = i

        return results

    # @override
    def __len__(self) -> int:
        return len(self._new_cache) + sum(len(record) for record in self._cache)

    # @override
    def __iter__(self) -> Iterator[_KT]:
        all_cache: _Record[_KT, _VT] = copy.deepcopy(self._new_cache)
        for record in self._cache:
            all_cache.update(record)

        return iter(all_cache)

    # @override
    def __setitem__(self, key: _KT, value: _VT) -> None:
        if key not in self._key_to_row_index:
            self._new_cache[key] = value
            return

        i: _Index = self._key_to_row_index[key]
        self._cache[i][key] = value

    # @override
    def __getitem__(self, key: _KT) -> _VT:
        if key in self._new_cache:
            return self._new_cache[key]

        i: _Index = self._key_to_row_index[key]
        return self._cache[i][key]

    # @override
    def __delitem__(self, key: _KT) -> None:
        if key in self._new_cache:
            del self._new_cache[key]
            return

        i: _Index = self._key_to_row_index[key]
        del self._cache[i][key]

    def filter_items(self, keys: Set[_KT]) -> None:
        """Filter keys that don't exist in the platform from the cache."""
        c: _Cache = copy.deepcopy(self._cache)
        for i, record in enumerate(c):
            self._cache[i] = {k: v for k, v in list(record.items()) if k in keys}

    def push_local_to_external(self) -> None:
        """Push the local cache of this object to the external cache storage."""
        self._distribute_new_cache_to_fill_existing_cache_and_push()
        self._distribute_new_cache_to_new_rows_and_push()

    def _distribute_new_cache_to_fill_existing_cache_and_push(self) -> None:
        self._distribute_new_items_to_unfilled_existing_rows()
        self._push_regular_cache()

    def _distribute_new_items_to_unfilled_existing_rows(self) -> None:
        row_indexes: Iterable[_Index] = self._get_indexes_sorted_by_content_length()
        for i in row_indexes:
            self._fill_row_with_new_items(self._cache[i])

    def _get_indexes_sorted_by_content_length(self) -> Iterable[_Index]:
        indexes: list[_Index] = list(range(len(self._cache)))
        return sorted(indexes, key=lambda i: len(_dump_property_value(self._cache[i])))

    def _fill_row_with_new_items(self, row: _Record[_KT, _VT]) -> None:
        dumped_row: JsonStr = _dump_property_value(row)
        while self._row_can_be_filled(dumped_row):
            _move_item(from_=self._new_cache, to=row)
            dumped_row = _dump_property_value(row)

        if _row_is_too_long(dumped_row):
            _move_item(from_=row, to=self._new_cache)

    def _row_can_be_filled(self, dumped_row: JsonStr) -> bool:
        return self._new_cache and not _row_is_too_long(dumped_row)

    def _push_regular_cache(self) -> None:
        for i, record in enumerate(self._cache):
            self._set_scoped_job_context_property(i, record)

    def _distribute_new_cache_to_new_rows_and_push(self) -> None:
        while self._new_cache:
            self._largest_row_index += 1
            self._remove_new_cached_items_and_save_them_to_row(self._largest_row_index)

    def _remove_new_cached_items_and_save_them_to_row(self, index: _Index) -> None:
        removed_keys: _Record[_KT, _VT] = {}
        new_cache: _Record[_KT, _VT] = copy.deepcopy(self._new_cache)
        while new_cache:
            try:
                self._set_scoped_job_context_property(index, new_cache)
                break

            except SiemplifyBase.MaximumContextLengthException:
                _move_item(from_=new_cache, to=removed_keys)

        self._new_cache = removed_keys

    def _get_scoped_job_context_property(self, index: _Index) -> JsonStr | None:
        key: str = _row_key(index)
        return self._context.get_context(key)

    def _set_scoped_job_context_property(self, index: _Index, cache: _Record) -> None:
        key: str = _row_key(index)
        value: JsonStr = _dump_property_value(cache)
        self._context.set_context(key, value)


def _load_record(row_value: JsonStr, /) -> _Record:
    _record: _Record = {}
    if row_value:
        _record = json.loads(row_value)

    return _record


def _row_is_too_long(row: JsonStr) -> bool:
    return len(row) >= SiemplifyUtils.MAXIMUM_PROPERTY_VALUE - ROW_PADDING_LENGTH


def _move_item(*, from_: _Record[_KT, _VT], to: _Record[_KT, _VT]) -> None:
    to.update([from_.popitem()])


def _row_key(_i: _Index, /) -> str:
    return CONTEXT_MOD_TIME_KEY.format(_i)


def _dump_property_value(__v, /) -> JsonStr:
    return json.dumps(__v, separators=(",", ":"))
