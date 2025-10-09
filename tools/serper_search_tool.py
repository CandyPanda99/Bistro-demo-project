from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import tool

search = GoogleSerperAPIWrapper()

@tool
def serper_search_tool(query: str) -> str:
    """
    This tool is used to get information from the web using Google. Call this for up-to-date information (also for things like Currency conversions, weather, news, sports scores, stock prices, etc.).
    :param query: The query to search for.
    :return: The response from the search.
    """
    return search.run(query)