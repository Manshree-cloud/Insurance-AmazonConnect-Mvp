# MVP Insurance Contact Center

This repository contains an MVP (minimum viable product) insurance contact‑centre built on top of **Amazon Connect**.  It demonstrates how a small team can assemble a feature‑rich IVR using cloud‑native services like Connect, Lex and Lambda.  The goal is to showcase the type of solution that someone with **six months to one year of AWS and contact centre experience** could build and operate.

## Overview

Customers can phone the contact centre to reach the **Auto**, **Home**, **Claims** or **Technical Support** queues.  Callers are greeted with a welcome message and can either press a key on their phone (DTMF) or speak naturally.  When a caller speaks, a **Lex V2 bot** interprets the intent and returns it to Connect.  A **Lambda function** is used to handle Lex responses and deliver dynamic prompts.

If all agents are busy, the system will offer to call the customer back.  A callback can be scheduled automatically and the customer will be removed from the queue.  Flow logging is enabled to help with troubleshooting.

## Architecture

The high‑level architecture looks like this:

- **Amazon Connect Instance:** Hosts the contact centre.  Contact flows route calls to queues or to Lex via Lambda.
- **Amazon Lex V2:** Receives spoken input from callers and interprets intents such as “claim status” or “policy information”.
- **AWS Lambda:** Acts as a simple backend.  In this MVP the Lambda function returns a message based on the Lex intent.  You can extend it to integrate with external systems such as policy databases or claims systems.
- **CloudWatch Logs and Metrics:** Connect automatically publishes metrics and logs.  Example CloudWatch charts are provided in the docs.

The main contact flow used by this project (`mvp_main_contactflow.json`) is included under [`contact‑flows/`](contact-flows/).  You can import this JSON into your Connect instance using the Connect console.

## Repository Structure

| Path | Description |
|-----|-------------|
| `contact-flows/` | Contact flow definitions exported from Amazon Connect as JSON.  Currently includes `mvp_main_contactflow.json` for the main IVR flow. |
| `docs/` | Screenshots and diagrams for the project.  These illustrate the agent console, Lex configuration, callback flow, and sample CloudWatch dashboards. |
| `lambda/` | Placeholder for Lambda functions used by the project.  A sample `lex_handler.py` will be added once available. |
| `lex/` | (Optional) Definitions or scripts related to Lex bots.  You can add Lex bot JSON here if exporting your own bot. |

## Getting Started

1. **Clone this repository** or download the files manually.

2. **Import the Contact Flow:**
   - Sign in to your Amazon Connect instance.
   - Navigate to *Contact Flows* and choose **Import flow**.
   - Upload `mvp_main_contactflow.json` from the `contact‑flows` directory.
   - Save and publish the flow.

3. **Deploy the Lambda Function:**
   - Navigate to the AWS Lambda console and create a new function (Python 3.x runtime) named `ABINS-LexHandler`.
   - Paste the contents of `lambda/lex_handler.py` (placeholder for now) into the editor or upload a zip.
   - Update your contact flow to reference the function ARN if you change the name.

4. **Configure Lex:**
   - Build a Lex V2 bot named `MvpInsurance-LexBot` with intents for `CheckClaimStatus` and `policyinformation`.
   - Deploy an alias named `Prod` and note its ARN.
   - Update the Lex settings in the contact flow if your bot/alias names differ.

5. **Test the IVR:**  Call your Connect telephone number and follow the prompts.  Use DTMF or voice commands to navigate.  Review the logs and metrics in Amazon CloudWatch to understand call flows.

## Screenshots

The `docs/` folder contains a number of screenshots to aid in understanding the solution:

| File | Description |
|-----|-------------|
| `agent_profile.png` | Example of an agent profile view in Amazon Connect. |
| `agent_workspace.png` | The Connect agent workspace showing call details and controls. |
| `amazon_lex.png` | Lex V2 configuration screen showing intents and slots. |
| `callback_flow.png` | Visual contact flow for handling callback offers. |
| `cloudwatch1.png` | Sample CloudWatch dashboard with call metrics. |
| `connect.png` | Entry point to the Connect instance. |
| `contactsearch.png` | Searching for contacts in the Connect console. |
| `cw_api.png`, `cw_g.png`, `cw_metric.png` | Additional CloudWatch metric views illustrating API usage and generic metrics. |
| `cw_metric3.png` | Yet another CloudWatch metric chart for extended performance analysis. |
| `cw_summary.png` | Consolidated CloudWatch summary chart showing multiple call metrics. |
| `cw_metric2.png` | Another CloudWatch metric example for deeper analysis. |
| `iam_lex.png` | IAM policy configuration used to grant Lex permissions. |
| `iam_lextest.png` | Screenshot of testing IAM permissions for the Lex bot. |
| `iam_role.png` | The IAM role associated with your Connect instance or Lambda. |
| `lambda_overview.png` | Overview of the Lambda function details in the AWS console. |
| `lambda_exe.png` | Lambda execution and configuration settings. |
| `lex_bot.png` | Summary of the Lex bot definition including intents. |
| `lex_intent.png` | Detailed configuration of a Lex intent. |
| `live_call.png` | Example of a live call in progress within Amazon Connect. |
| `logstream.png`, `logstream1.png` | CloudWatch Log Streams showing real‑time logs for Lambda or Connect. |
| `metric1.png` | Another CloudWatch metric chart to complement the existing metrics. |
| `mvp_customerqueue.png` | Diagram or screenshot of the customer queue configuration for the MVP. |
| `mvp_main_contact_flow.png` | Visual representation of the main contact flow used in this project. |
| `performance_dashboard.png` | Performance dashboard illustrating key call centre KPIs. |
| `prod_lex.png` | Production alias configuration for the Lex bot. |
| `real_time_agent_metrics.png` | Real‑time agent metrics dashboard from Amazon Connect. |
| `routing_profile.png` | Routing profile settings used to map agents to queues. |
| `s3_connect.png` | S3 bucket configuration used for storing call recordings or exports. |
| `s3_connect_recordingbucket.png` | Specific recording bucket configuration for Connect call recordings. |

## Extending the MVP

The current implementation is intentionally minimal.  To extend it:

- Add more intents to the Lex bot for other self‑service scenarios such as “make a payment” or “update address”.
- Integrate the Lambda handler with external APIs or databases to return live policy or claim information.
- Use **Amazon Connect Tasks** to follow up with customers asynchronously.
- Build CloudWatch dashboards or alarms to monitor queue length, callback rate and agent availability.

Contributions are welcome!  Feel free to fork the repository and submit pull requests for enhancements.