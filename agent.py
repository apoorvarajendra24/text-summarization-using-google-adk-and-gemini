import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.langchain_tool import LangchainTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

import google.auth
import google.auth.transport.requests
import google.oauth2.id_token

# --- Setup Logging and Environment ---

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()

model_name = os.getenv("MODEL")

# Greet user and save their prompt
def add_prompt_to_state(
    tool_context: ToolContext, prompt: str
) -> dict[str, str]:
    """Saves the user's input text to the state."""
    tool_context.state["PROMPT"] = prompt
    logging.info(f"[State updated] Added to PROMPT: {prompt}")
    return {"status": "success"}

# 1. Summarization Agent (replaces researcher)
text_summarizer = Agent(
    name="text_summarizer",
    model=model_name,
    description="Summarizes input text.",
    instruction="""
    You are an AI agent specialized in text summarization.

    Summarize the following text into 3 concise lines.
    Do not add extra explanation.

    TEXT:
    {prompt}
    """,
    tools=[],
    output_key="summary_data"
)

# 2. Response Formatter Agent (keep structure same)
response_formatter = Agent(
    name="response_formatter",
    model=model_name,
    description="Formats output.",
    instruction="""
    Present the summary clearly.

    SUMMARY:
    { summary_data }
    """
)

# Main Workflow (UNCHANGED STRUCTURE)
tour_guide_workflow = SequentialAgent(
    name="text_summarization_workflow",
    description="Workflow for summarizing user input text.",
    sub_agents=[
        text_summarizer,     # Step 1: Generate summary
        response_formatter,  # Step 2: Format output
    ]
)

root_agent = tour_guide_workflow
