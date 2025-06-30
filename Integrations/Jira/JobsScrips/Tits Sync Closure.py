from datetime import timezone

from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler, convert_datetime_to_unix_time, unix_now
from TIPCommon import extract_action_param
from TIPCommon import get_last_success_time

from JiraConstants import (
    JIRA_CLOSED_STATUS,
    JIRA_ISSUE_KEY,
    JIRA_PROJECT_KEY,
    PRODUCT,
    JIRA_TAG,
    SYNC_CLOSURE_SCRIPT,
    ROOT_CAUSE,
    REASON,
    COMMENT,
    JIRA_TIME_FORMAT,
    CASE_STATUS_OPEN,
    MIN_DAYS_BACKWARDS,
)
from JiraManager import JiraManager
from exceptions import JiraManagerError
from utils import get_case_and_alert_ids_for_issue_key, load_csv_to_list


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.API_ROOT = "https://him:8443/api"
    siemplify.script_name = SYNC_CLOSURE_SCRIPT
    siemplify.LOGGER.info("--------------- JOB STARTED ---------------")

    api_root = extract_action_param(
        siemplify=siemplify, param_name="API Root", is_mandatory=True, print_value=True
    )
    username = extract_action_param(
        siemplify=siemplify, param_name="Username", is_mandatory=True, print_value=True
    )
    api_token = extract_action_param(
        siemplify=siemplify,
        param_name="API Token",
        is_mandatory=True,
        print_value=False,
    )
    project_names = extract_action_param(
        siemplify=siemplify,
        param_name="Project Names",
        is_mandatory=False,
        print_value=True,
    )
    environment_ = extract_action_param(
        siemplify=siemplify,
        param_name="Environment",
        print_value=True,
    )
    environments = [environment_] if environment_ else []

    try:
        days_backwards = extract_action_param(
            siemplify=siemplify,
            param_name="Days Backwards",
            input_type=int,
            is_mandatory=True,
            print_value=True,
        )
        project_names = load_csv_to_list(project_names, "Project Names")
        fetch_time = get_last_success_time(
            siemplify, offset_with_metric={"days": days_backwards}, print_value=False
        )
        fetch_time_ms = convert_datetime_to_unix_time(fetch_time)
        siemplify.LOGGER.info(
            f"Last fetch time. Date time:{fetch_time}. Unix:{fetch_time_ms}"
        )
        new_timestamp = unix_now()

        if days_backwards < MIN_DAYS_BACKWARDS:
            raise Exception(
                f'"Days Backwards" parameter must be greater or equal than {MIN_DAYS_BACKWARDS}'
            )

        jira_manager = JiraManager(api_root, username, api_token)

        filtered_closed_cases = []
        closed_alerts_issue_keys = []

        for project_name in project_names:
            try:
                siemplify.LOGGER.info(
                    f"Fetching ticket ids for closed cases of project {project_name}"
                )
                ticket_ids_for_closed_cases = (
                    siemplify.get_alerts_ticket_ids_from_cases_closed_since_timestamp(
                        fetch_time_ms,
                        None,
                    )
                )
                siemplify.LOGGER.info(
                    f"Successfully fetched {len(ticket_ids_for_closed_cases)} ticket ids of closed cases with rule "
                    f"since {fetch_time_ms} (Unix)"
                )
                for ticket_id in ticket_ids_for_closed_cases:
                    try:
                        cases_ids = siemplify.get_cases_by_filter(
                            environments=environments,
                            ticked_ids_free_search=ticket_id,
                            tags=[JIRA_TAG],
                        )
                        filtered_closed_cases.extend(
                            [
                                siemplify._get_case_by_id(case_id)
                                for case_id in cases_ids
                            ]
                        )
                    except Exception as e:
                        siemplify.LOGGER.error(
                            f"Failed to fetch case with ticket id {ticket_id}. Reason {e}"
                        )
            except Exception as error:
                siemplify.LOGGER.error(
                    f"Failed to get alert ticket ids from closed cases since last fetch time for project {project_name}"
                )
                siemplify.LOGGER.exception(error)

        siemplify.LOGGER.info(
            f"Found {len(filtered_closed_cases)} closed cases with tag {JIRA_TAG} since last fetch time"
        )
        siemplify.LOGGER.info("--- Start Closing Issues in Jira ---")

        for case in filtered_closed_cases:
            for alert in case.get("cyber_alerts", []):
                issue_key = (
                    alert.get("additional_data")
                    if alert.get("reporting_product") != PRODUCT
                    else alert.get("additional_properties", {}).get("AlertName")
                )
                if not issue_key:
                    issue_key = siemplify.get_context_property(
                        2,
                        alert.get("alert_group_identifier"),
                        JIRA_ISSUE_KEY,
                    )

                issue_project = (
                    alert.get("security_events", [])[0]
                    .get("additional_properties", {})
                    .get("project_name")
                )
                if not issue_project:
                    issue_project = siemplify.get_context_property(
                        2,
                        alert.get("alert_group_identifier"),
                        JIRA_PROJECT_KEY,
                    )

                if issue_key:
                    try:
                        siemplify.LOGGER.info(
                            f"Updating issue {issue_key} of project {issue_project} to status {JIRA_CLOSED_STATUS}"
                        )
                        jira_manager.update_issue(issue_key, status=JIRA_CLOSED_STATUS)
                        siemplify.LOGGER.info(
                            f"Jira issue - {issue_key} status was updated to {JIRA_CLOSED_STATUS}"
                        )
                        closed_alerts_issue_keys.append(issue_key)
                    except JiraManagerError as error:
                        siemplify.LOGGER.error(
                            f"Failed to update issue {issue_key} with status {JIRA_CLOSED_STATUS}. It might be already closed"
                        )
                        siemplify.LOGGER.exception(error)

        siemplify.LOGGER.info(
            "--- Finish synchronize closure from Siemplify to Jira issues ---"
        )

        siemplify.LOGGER.info("--- Start Closing Alerts in Siemplify ---")

        # Adjust fetch time to JIRA server's timezone
        jira_server_time = jira_manager.get_server_time()
        siemplify.LOGGER.info(f"JIRA server time: {jira_server_time.isoformat()}")
        fetch_time_jira_timezone_adjusted = fetch_time.replace(
            tzinfo=timezone.utc
        ).astimezone(jira_server_time.tzinfo)
        siemplify.LOGGER.info(
            f"Adjusted last fetch time to server time: {fetch_time_jira_timezone_adjusted.isoformat()}"
        )

        # Fetched closed issues from Jira
        jira_last_time_format = fetch_time_jira_timezone_adjusted.strftime(
            JIRA_TIME_FORMAT
        )
        done_issues = jira_manager.list_issues(
            updated_from=jira_last_time_format,
            status_list=[JIRA_CLOSED_STATUS],
            project_key_list=project_names,
        )
        siemplify.LOGGER.info(
            f"Found {len(done_issues)} {JIRA_CLOSED_STATUS} issues since {fetch_time_jira_timezone_adjusted.isoformat()} (Server Timezone)"
        )

        for issue_key in done_issues:
            # Filter already close alerts
            siemplify.LOGGER.info(f"DONE ISSUES:{done_issues}")
            siemplify.LOGGER.info(f"ISSUE KEY:{issue_key}")
            siemplify.LOGGER.info(f"CLOSED ISSUES:{closed_alerts_issue_keys}")
            if issue_key in closed_alerts_issue_keys:
                continue

            # Find open siemplify cases that needs to be closed
            cases_ids_for_issue = siemplify.get_cases_by_filter(
                environments=environments,
                ticked_ids_free_search=issue_key,
                tags=[JIRA_TAG],
                statuses=[CASE_STATUS_OPEN],
            )
            if not cases_ids_for_issue:
                fetched_open_cases_ids = siemplify.get_cases_by_filter(
                    environments=environments,
                    statuses=[CASE_STATUS_OPEN],
                    tags=[JIRA_TAG],
                )
                case_details = {}
                for case_id in fetched_open_cases_ids:
                    case = siemplify._get_case_by_id(case_id)
                    case_alerts = case.get("cyber_alerts", [])
                    case_details[case_id] = case_alerts

                cases_ids_for_issue = list(
                    {
                        case_id
                        for case_id, _ in get_case_and_alert_ids_for_issue_key(
                            case_details=case_details,
                            issue_key=issue_key,
                            chronicle_soar=siemplify,
                        )
                    }
                )

            if not cases_ids_for_issue:
                siemplify.LOGGER.info(
                    f"No open siemplify cases were found for issue key {issue_key} and tag {JIRA_TAG}"
                )
                continue

            for case_id in cases_ids_for_issue:
                case_obj = siemplify._get_case_by_id(case_id)
                if case_obj:
                    # Get case alerts to close
                    case_alerts = case_obj.get("cyber_alerts", [])

                    # Find alerts with matching tag and alert identifier matching closed jira issue
                    alerts_to_close = [
                        (case_obj.get("identifier"), alert.get("identifier"))
                        for alert in case_alerts
                        if issue_key
                        in [alert.get("external_id"), alert.get("additional_data")]
                    ] or get_case_and_alert_ids_for_issue_key(
                        case_details=case_details,
                        issue_key=issue_key,
                        chronicle_soar=siemplify,
                    )

                    for case_obj_id, alert_id in alerts_to_close:
                        try:
                            siemplify.LOGGER.info(
                                f"Closing alert {alert_id} with case id {case_id} of issue key {issue_key}"
                            )
                            siemplify.close_alert(
                                root_cause=ROOT_CAUSE,
                                reason=REASON,
                                comment=COMMENT,
                                case_id=case_obj_id,
                                alert_id=alert_id,
                            )
                            siemplify.LOGGER.info(
                                f"Alert with issue key {issue_key} was closed"
                            )
                        except Exception as error:
                            siemplify.LOGGER.error(
                                f"Failed to close alert {alert_id} of case {case_obj_id}"
                            )
                            siemplify.LOGGER.exception(error)

        siemplify.save_timestamp(new_timestamp=new_timestamp)
        siemplify.LOGGER.info(
            " --- Finish synchronize closure from Jira to Siemplify alerts --- "
        )
        siemplify.LOGGER.info("--------------- JOB FINISHED ---------------")

    except (JiraManagerError, Exception) as error:
        siemplify.LOGGER.error(f"Got exception on main handler. Error: {error}")
        siemplify.LOGGER.exception(error)
        raise


if __name__ == "__main__":
    main()
