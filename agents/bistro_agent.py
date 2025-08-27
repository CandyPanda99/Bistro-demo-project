from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate

from constants.prompts import BISTRO_AGENT_SYSTEM_PROMPT
from models.chat_models.chat_openai import get_openai_chat
from tools.ddg_search_tool import ddg_search
from tools.information_tool import lookup_information
from tools.menu_agent_tool import menu_agent_tool

llm = get_openai_chat()

tools = [
    ddg_search,
    lookup_information,
    menu_agent_tool
]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            BISTRO_AGENT_SYSTEM_PROMPT,
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

bistro_assistant_runnable = prompt | llm.bind_tools(tools)

