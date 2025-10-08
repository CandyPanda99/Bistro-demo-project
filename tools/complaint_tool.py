import json
import os

from langchain_core.tools import tool

from schemas.complaint import Complaint

data_dir = "./data"
complaints_file = os.path.join(data_dir, "complaints.json")

@tool
def complaint_tool(complaint: Complaint) -> str:
    """
    This tool is used to make complaints about experiences.
    :param complaint: The complaint to be made.
    :return: A confirmation that the complaint has been received.
    """

    missing_fields = []
    if not complaint.name:
        missing_fields.append("name")
    if not complaint.contact_number:
        missing_fields.append("contact_number")
    if not complaint.complaint_details:
        missing_fields.append("complaint_details")

    if missing_fields:
        return f"Failed to make reservation. The following fields are missing: {', '.join(missing_fields)}"

    complaint_dict = complaint.model_dump()

    try:
        with open(complaints_file, "r+") as f:
            reservations = json.load(f)
            reservations.append(complaint_dict)
            f.seek(0)
            json.dump(reservations, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(complaints_file, "w") as f:
            json.dump([complaint_dict], f, indent=4)

    print(complaint)
    return f"Complaint received for order {complaint.name}. We will get back to you shortly."