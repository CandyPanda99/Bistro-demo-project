from langchain_core.tools import tool

from schemas.complaint import Complaint


@tool
def complaint_tool(complaint: Complaint) -> str:
    """
    This tool is used to make complaints about experiences.
    :param complaint: The complaint to be made.
    :return: A confirmation that the complaint has been received.
    """
    print(complaint)
    return f"Complaint received for order {complaint.name}. We will get back to you shortly."