from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS

from reels_tools import get_creator_transcriptions, list_available_creators
from dotenv import load_dotenv
load_dotenv()


copywriter = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    name="copywriter",

    add_history_to_context=True,
    num_history_runs=10,
    db=SqliteDb(session_table="agent_sessions", db_file="tmp/storage.db"),

    tools=[
        TavilyTools(),
        list_available_creators,
        get_creator_transcriptions,
    ],
    instructions=open("prompts/copywriter.md").read(),
)

agent_os = AgentOS(agents=[copywriter])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agent:app")
