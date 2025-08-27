from pydantic import BaseModel, Field


class Reservation(BaseModel):
    """Represents a user with their personal information."""
    name: str = Field(default=None, description="The user's full name.")
    contact_number: str = Field(default=None, description="Contact information ex: +94712578293 (should include country code if not included, assume +94)")
    number_of_guests: int = Field(default=1, description="Number of guests the reservation should be for")
    special_requests: str = Field(default=None, description="Any special requests for the reservation")