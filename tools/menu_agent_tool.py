from agents.menu_agent import menu_agent_executor
from langchain.agents import tool


@tool
def menu_agent_tool(query: str) -> str:
    """
    This tool is used to get information about the menu.
    :param query: The query to ask the menu agent.
    :return: The response from the menu agent.
    """
    return menu_agent_executor.invoke({"input": query})
