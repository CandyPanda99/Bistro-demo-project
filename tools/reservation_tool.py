import json
import os
from langchain_core.tools import tool

from schemas.reservation import Reservation

data_dir = "./data"
reservations_file = os.path.join(data_dir, "reservations.json")


@tool
def reservation_tool(reservation: Reservation) -> str:
    """
    This tool is used to make reservations at the restaurant.
    :param reservation:
    :return: A confirmation that the reservation has been received.
    """
    missing_fields = []
    if not reservation.name:
        missing_fields.append("name")
    if not reservation.contact_number:
        missing_fields.append("contact_number")
    if not reservation.number_of_guests:
        missing_fields.append("number_of_guests")
    if not reservation.reservation_date:
        missing_fields.append("reservation_date")
    if not reservation.meal_type:
        missing_fields.append("meal_type")

    if missing_fields:
        return f"Failed to make reservation. The following fields are missing: {', '.join(missing_fields)}"

    reservation_dict = reservation.model_dump()
    reservation_dict['reservation_date'] = reservation_dict['reservation_date'].isoformat()

    try:
        with open(reservations_file, "r+") as f:
            reservations = json.load(f)
            reservations.append(reservation_dict)
            f.seek(0)
            json.dump(reservations, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(reservations_file, "w") as f:
            json.dump([reservation_dict], f, indent=4)

    return f"Reservation confirmed for {reservation.name}"