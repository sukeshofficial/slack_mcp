from agno.agent import Agent
from agno.tools.slack import SlackTools
from agno.models.openrouter import OpenRouter
import os
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenRouter(
        id="gpt-4o-mini",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    ),
    tools=[SlackTools(
        token=os.getenv("SLACK_TOKEN"),
        send_message=True,
        list_channels=True,
        get_channel_history=True
    )],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Send a message to the Slack channel with the ID C08RRLXDBFG saying 'Hello I'm SUKESH - msg sent by AGENT'.")