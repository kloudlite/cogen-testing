from agentman import tool, action

@tool(
  "gmail",
  description="Tool to send emails", 
  parameters={"email": "Email address"},
  required=["email"],
  category="communication"
)
class GmailTool:
  def __init__(self):
      return self

  @action(
    "send_email",
    description="Send an email", 
    parameters={
      "to": {"type": "string", "description": "Email address to send the email to"},
      "subject": {"type": "string", "description": "Subject of the email"},
      "body": {"type": "string", "description": "Body of the email"}
    },
    required=["subject", "body"]
  )
  def send_email(self, to: str, subject: str, body: str):
      print(f"Sending email to {to} with subject: {subject} and body: {body}")
      return "Email sent"