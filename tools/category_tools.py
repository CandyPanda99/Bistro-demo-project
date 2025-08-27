from langchain.agents import tool
import json

@tool
def get_beverages_menu() -> str:
    """
    This tool is used to get the beverages menu.
    :return: A string containing the beverages menu in JSON format.
    """
    with open("./data/menus/beverages.json", "r") as f:
        return json.load(f)

@tool
def get_appetizers_menu() -> str:
    """
    This tool is used to get the appetizers and soups menu.
    :return: A string containing the appetizers and soups menu in JSON format.
    """
    with open("./data/menus/appetizers.json", "r") as f:
        return json.load(f)

@tool
def get_curries_menu() -> str:
    """
    This tool is used to get the curries menu.
    :return: A string containing the curries menu in JSON format.
    """
    with open("./data/menus/curries.json", "r") as f:
        return json.load(f)

@tool
def get_mains_menu() -> str:
    """
    This tool is used to the main courses menu/
    :return: A string containing main course menu in JSON format.
    """
    with open("./data/menus/mains.json", "r") as f:
        return json.load(f)


@tool
def get_desserts_menu() -> str:
    """
    This tool is used to get the desserts menu.
    :return: A string containing the desserts menu in JSON format.
    """
    with open("./data/menus/desserts.json", "r") as f:
        return json.load(f)

