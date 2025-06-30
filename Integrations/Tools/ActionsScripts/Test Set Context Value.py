from ScriptResult import EXECUTION_STATE_COMPLETED
from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import output_handler


GLOBAL_CONTEXT = 0
IDENTIFIER = "GLOBAL"


def set_global_context(smp, key, value):
    smp.set_context_property(GLOBAL_CONTEXT, IDENTIFIER, key, value)


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.API_ROOT = "https://him:8443/api"

    scope = siemplify.extract_action_param("Scope")
    key = siemplify.extract_action_param("Key")
    value = siemplify.extract_action_param("Value")

    if scope == "Alert":
        siemplify.set_alert_context_property(key, value)
    elif scope == "Case":
        siemplify.set_case_context_property(key, value)
    elif scope == "Global":
        set_global_context(siemplify, key, value)

    output_message = (
        f"Successfully Updated field {key} with value '{value}' in scope {scope}."
    )

    siemplify.end(output_message, True, EXECUTION_STATE_COMPLETED)


if __name__ == "__main__":
    main()
