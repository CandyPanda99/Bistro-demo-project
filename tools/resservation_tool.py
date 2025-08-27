from langchain_core.tools import tool

from schemas.reservation import Reservation


@tool
def reservation_tool(reservation: Reservation) -> str:
    """
    This tool is used to make reservations at the restaurant.
    :param query: The query to ask the menu agent.
    :return: The response from the menu agent.
    """
    print(reservation)
    return "Reservation confirmed for {reservation.name} on {reservation.date} at {reservation.time} for {reservation.party_size} people. Contact: {reservation.contact_info}."