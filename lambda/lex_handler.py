import json
from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, str]:
    intent = (
        event.get("Details", {})
        .get("ContactData", {})
        .get("Attributes", {})
        .get("action", "")
    )

    responses = {
        "CheckClaimStatus": "Your claim is currently being processed. An agent will reach out to you soon.",
        "policyinformation": "Your policy details will be sent to your registered email address shortly.",
    }

    message = responses.get(
        intent,
        "Thank you for calling MVP Insurance. An agent will assist you shortly."
    )

    return {"message": message}
