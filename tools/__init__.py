class SampleTool:
  """
    A sample tool class.
  """
  
  def __init__(self, apiKey:str, clientId:str):
    self.clientId = clientId
    self.apiKey = apiKey

  def say_hello(self):
    """
      This is say hello funciton. This won't do anything other than responding hello.
    """
    print(f'Hello, {self.name}!')

  
  def sendEmail(self, to, subject, message):
    """
      This function will send an email to the recipient.
    """
    print(f'Sending email to {to} with subject {subject} and message {message}')