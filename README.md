# 📞 Insurance Contact Center – Amazon Connect MVP

Production-style **Amazon Connect contact center MVP** built for an insurance use case, demonstrating **end-to-end IVR design, Lex integration, Lambda automation, monitoring, and operational visibility**.

This project reflects **hands-on experience designing, configuring, and operating Amazon Connect workloads** with a focus on real-world support and production readiness.

---
🏗 High-Level Call Flow (Logic First)
Customer calls Insurance Support
        ↓
Amazon Connect Entry Point
        ↓
Welcome Prompt (Voice + DTMF)
        ↓
DTMF OR Amazon Lex (Voice Intent)
        ↓
Lambda (Python business logic)
        ↓
Correct Queue (Auto / Home / Claims / Tech)
        ↓
Agent Workspace
        ↓
Call Recording + Metrics + Logs


This flow intentionally supports both keypad users and voice users, which is critical in real insurance contact centers.

🧠 Core Amazon Connect Logic (Detailed)
1️⃣ Entry Point & Logging

Call enters Amazon Connect contact flow

Flow logging enabled immediately for traceability

Ensures all execution steps are visible in CloudWatch Logs

📸 Proof


2️⃣ Welcome Prompt + Menu Design

Customer hears a structured welcome message

Options available via:

DTMF (keypad)

Voice (Amazon Lex)

This design avoids hard dependency on voice only (common real-world requirement).

📸 Proof


3️⃣ DTMF Routing (Fallback-Safe Design)

Key presses route directly to queues:

1 → Auto Insurance

2 → Home Insurance

3 → Claims (Lex-enabled path)

4 → Technical Support

Handles:

No input

Invalid input

Timeouts

This ensures callers never get stuck.

📸 Proof


4️⃣ Amazon Lex (Voice Intent Handling)

Lex is used only where voice adds value (Claims & Policy queries).

Lex V2 bot trained with intents:

CheckClaimStatus

PolicyInformation

Lex collects intent → passes context to Lambda

Contact flow evaluates $.Lex.IntentName

📸 Proof




5️⃣ Python Lambda (Business Logic)

Lambda is where decision-making happens, not in the IVR.

Written in Python

Receives intent from Lex

Performs logic based on intent type

Returns structured responses back to Amazon Connect

This separation keeps:

Contact flows readable

Business logic version-controlled

📸 Proof




6️⃣ Queue Routing & Agent Experience

Calls are routed to insurance-specific queues

Routing profiles ensure correct agent selection

Agent Workspace shows real-time call context

📸 Proof




7️⃣ Queue Capacity & Callback Handling

If a queue is full:

Customer is offered a callback

Callback number is captured dynamically

Prevents excessive wait times

📸 Proof


📊 Monitoring, Logs & Operations (Very Important)
CloudWatch Logs

Contact flow execution logs

Lambda invocation logs

Enables post-incident analysis

📸 Proof


CloudWatch Metrics & Dashboards

Queue depth

Agent availability

Call performance

Real-time operational visibility

📸 Proof




🔐 IAM & Security

Separate IAM roles for:

Amazon Connect

Lex

Lambda

Permissions scoped to least privilege

No credentials stored in repo

📸 Proof


📂 Repository Structure
Insurance-AmazonConnect-Mvp/
├── contact-flows/
│   └── mvp_main_contactflow.json
│
├── lambda/
│   └── lex_handler.py
│
├── docs/
│   ├── (all screenshots & proofs)
│
└── README.md


All additional screenshots and detailed proofs are available in the /docs folder.

🎯 Key Skills Demonstrated

Amazon Connect IVR design

DTMF + Voice hybrid routing

Amazon Lex V2 integration

Python Lambda development

CloudWatch monitoring & troubleshooting

Production-style error handling

Contact center operational thinking

🚀 Why This Matters

This project is not a demo flow — it reflects how real insurance contact centers are designed, monitored, and supported using Amazon Connect.

👤 Author: Manshree Patel
🎯 Focus: Amazon Connect | AWS | Serverless










































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
