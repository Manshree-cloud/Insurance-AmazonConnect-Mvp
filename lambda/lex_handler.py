"""
Example Lambda function used by the MVP Insurance Contact Centre.

This function is invoked by the contact flow via the **InvokeLambdaFunction** block.  It
reads an `action` attribute (populated by the Lex bot or contact flow) and returns a
simple prompt for the caller.

In a real implementation you would replace the message lookup with calls to internal
systems (e.g. policy or claims databases) and construct a personalised response.
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

    # Safely extract the intent name/action from event attributes.
    # Lex sets this in `$.Lex.IntentName`, but the contact flow copies it to
    # `Attributes.action` via the `SaveLexIntent` block.
    intent_name = (
        event.get("Details", {})
        .get("ContactData", {})
        .get("Attributes", {})
        .get("action", "")
    )

    # Define simple canned responses for each supported intent.
    responses = {
        "CheckClaimStatus": (
            "Your claim is currently being processed. An agent will reach out to you soon."
        ),
        "policyinformation": (
            "Your policy details will be sent to your registered email address shortly."
        ),
    }

    # Fallback message if the intent is not recognised.
    default_response = "Thank you for calling MvpInsurance. An agent will assist you shortly."

    # Look up the response.
    prompt = responses.get(intent_name, default_response)

    # The contact flow expects a JSON object with a top‑level `message` field.
    return {"message": prompt}