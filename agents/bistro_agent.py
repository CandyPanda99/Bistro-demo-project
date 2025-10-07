from datetime import datetime

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from constants.prompts import BISTRO_AGENT_SYSTEM_PROMPT
from models.chat_models.chat_openai import get_openai_chat
from tools.serper_search_tool import serper_search_tool
from tools.complaint_tool import complaint_tool
from tools.information_tool import lookup_information
from tools.menu_agent_tool import menu_agent_tool
from tools.reservation_tool import reservation_tool

llm = get_openai_chat()

tools = [
    serper_search_tool,
    lookup_information,
    menu_agent_tool,
    reservation_tool,
    complaint_tool
]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            BISTRO_AGENT_SYSTEM_PROMPT,
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
).partial(time=datetime.now)

bistro_assistant_runnable = prompt | llm.bind_tools(tools)

