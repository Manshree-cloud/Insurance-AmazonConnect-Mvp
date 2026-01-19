"""
Lambda function used by the MVP Insurance Contact Centre.

This function is invoked by the contact flow via the **InvokeLambdaFunction** block.  It
reads an `action` attribute (populated by the Lex bot or contact flow) and returns a
simple prompt for the caller.


"""

import json
from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, str]:
    """Entry point for AWS Lambda.

    Parameters
    ----------
    event : dict
        The event from Amazon Connect.  It may contain details about the call and
        attributes set by Lex or the contact flow.
    context : Any
        Lambda context (unused).

    Returns
    -------
    dict
        A simple dictionary with a `message` key containing the prompt to play
        back to the caller.
    """


    intent_name = (
        event.get("Details", {})
        .get("ContactData", {})
        .get("Attributes", {})
        .get("action", "")
    )

    
    responses = {
        "CheckClaimStatus": (
            "Your claim is currently being processed. An agent will reach out to you soon."
        ),
        "policyinformation": (
            "Your policy details will be sent to your registered email address shortly."
        ),
    }

    default_response = "Thank you for calling MvpInsurance. An agent will assist you shortly."

    # Look up the response.
    prompt = responses.get(intent_name, default_response)

    # The contact flow expects a JSON object with a top‑level `message` field.
    return {"message": prompt}
