from agentman import tool, action

@tool
class GmailTool:
  def __init__(self, email: str, password: str):
    self.email = email
    self.password = password
    
  @action(
    description="Send an email", 
    parameters={
      "to": {"type": "string", "description": "Email address to send the email to"},
      "subject": {"type": "string", "description": "Subject of the email"},
      "body": {"type": "string", "description": "Body of the email"}
    }
  )
  def send_email(self, to: str, subject: str, body: str):
      print(f"Sending email to {to} with subject: {subject} and body: {body}")
      return "Email sent"