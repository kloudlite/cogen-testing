from agentman import tool, action
import requests
import json

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

@tool
class HackerNewsTool:
    def __init__(self,name: str):
        self.base_url = "https://hacker-news.firebaseio.com/v0"

    @action(
        description="Fetch top stories from Hacker News",
        parameters={
            "limit": {"type": "integer", "description": "Number of top stories to fetch (default: 10)"}
        }
    )
    def get_top_stories(self, limit: int = 10):
        """
        Fetches the top stories from Hacker News.
        :param limit: Number of top stories to fetch (default: 10).
        :return: List of top stories with their details.
        """
        try:
            # Fetch top story IDs
            top_stories_url = f"{self.base_url}/topstories.json"
            response = requests.get(top_stories_url)
            response.raise_for_status()
            top_story_ids = response.json()

            # Fetch details for the top `limit` stories
            stories = []
            for story_id in top_story_ids[:limit]:
                story_url = f"{self.base_url}/item/{story_id}.json"
                story_response = requests.get(story_url)
                story_response.raise_for_status()
                story_data = story_response.json()
                stories.append({
                    "title": story_data.get("title", "No title"),
                    "url": story_data.get("url", "No URL"),
                    "by": story_data.get("by", "Unknown author"),
                    "score": story_data.get("score", 0),
                    "time": story_data.get("time", 0),
                    "type": story_data.get("type", "story")
                })

            return json.dumps(stories, indent=2)
        except requests.exceptions.RequestException as e:
            return f"Failed to fetch data from Hacker News: {e}"

    @action(
        description="Fetch a specific story or comment from Hacker News by ID",
        parameters={
            "item_id": {"type": "integer", "description": "ID of the item to fetch"}
        }
    )
    def get_item(self, item_id: int):
        """
        Fetches a specific story or comment from Hacker News by its ID.
        :param item_id: ID of the item to fetch.
        :return: Details of the item.
        """
        try:
            item_url = f"{self.base_url}/item/{item_id}.json"
            response = requests.get(item_url)
            response.raise_for_status()
            item_data = response.json()
            return {
                "title": item_data.get("title", "No title"),
                "url": item_data.get("url", "No URL"),
                "by": item_data.get("by", "Unknown author"),
                "score": item_data.get("score", 0),
                "time": item_data.get("time", 0),
                "type": item_data.get("type", "story"),
                "text": item_data.get("text", "No text")
            }
        except requests.exceptions.RequestException as e:
            return f"Failed to fetch item from Hacker News: {e}"
        
