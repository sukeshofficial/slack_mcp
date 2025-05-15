import json
import os
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional

import logging

from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

load_dotenv()

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
except ImportError:
    raise ImportError("Slack tools require the `slack_sdk` package. Run `pip install slack-sdk` to install it.")

mcp = FastMCP("slack-server")

# Initialize Slack client
token = os.getenv("SLACK_TOKEN")
if not token:
    raise ValueError("SLACK_TOKEN environment variable not set")
client = WebClient(token=token)

@mcp.tool()
def send_message(channel: str, text: str) -> str:
    """
    Send a message to a Slack channel.

    Args:
        channel (str): The channel ID or name to send the message to
        text (str): The text of the message to send

    Returns:
        str: JSON response from Slack API
    """
    try:
        response = client.chat_postMessage(channel=channel, text=text)
        return json.dumps(response.data)
    except SlackApiError as e:
        logger.error(f"Error sending message: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
def list_channels() -> str:
    """
    List all channels in the Slack workspace.

    Returns:
        str: JSON list of channels with their IDs and names
    """
    try:
        response = client.conversations_list()
        channels = [{"id": channel["id"], "name": channel["name"]} 
                   for channel in response["channels"]]
        return json.dumps(channels)
    except SlackApiError as e:
        logger.error(f"Error listing channels: {e}")
        return json.dumps({"error": str(e)})

@mcp.tool()
def get_channel_history(channel: str, limit: int = 100) -> str:
    """
    Get the message history of a Slack channel.

    Args:
        channel (str): The channel ID to fetch history from
        limit (int): Maximum number of messages to fetch (default: 100)

    Returns:
        str: JSON array of channel messages
    """
    try:
        response = client.conversations_history(channel=channel, limit=limit)
        messages: List[Dict[str, Any]] = [
            {
                "text": msg.get("text", ""),
                "user": "webhook" if msg.get("subtype") == "bot_message" else msg.get("user", "unknown"),
                "ts": msg.get("ts", ""),
                "sub_type": msg.get("subtype", "unknown"),
                "attachments": msg.get("attachments", []) if msg.get("subtype") == "bot_message" else "n/a",
            }
            for msg in response.get("messages", [])
        ]
        return json.dumps(messages)
    except SlackApiError as e:
        logger.error(f"Error getting channel history: {e}")
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    mcp.run()
