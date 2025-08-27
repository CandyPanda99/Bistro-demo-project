from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent

from constants.prompts import MENU_AGENT_PROMPT
from models.chat_models.chat_openai import get_openai_chat

chat_openai_model = get_openai_chat()
from tools.category_tools import (
    get_beverages_menu,
    get_appetizers_menu,
    get_curries_menu,
    get_mains_menu,
    get_desserts_menu
)


tools = [
    get_beverages_menu,
    get_appetizers_menu,
    get_curries_menu,
    get_mains_menu,
    get_desserts_menu
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", MENU_AGENT_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

menu_agent = create_openai_tools_agent(chat_openai_model, tools, prompt)

menu_agent_executor = AgentExecutor(
    agent=menu_agent,
    tools=tools,
    verbose=True,
)

