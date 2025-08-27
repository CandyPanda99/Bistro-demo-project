from datetime import date
from enum import Enum
from pydantic import BaseModel, Field


class MealType(str, Enum):
    LUNCH = "lunch"
    BRUNCH = "brunch"
    DINNER = "dinner"


class Reservation(BaseModel):
    """Represents a user with their personal information."""
    name: str = Field(default=None, description="The user's full name.")
    contact_number: str = Field(default=None, description="Contact information ex: +94712578293 (should include country code if not included, assume +94)")
    number_of_guests: int = Field(default=1, description="Number of guests the reservation should be for")
    reservation_date: date = Field(..., description="The date of the reservation.")
    meal_type: MealType = Field(..., description="The type of meal (lunch, brunch, or dinner). (Sat and Sun only brunch and Dinner is available, Monday to friday only Lunch and dinner is available)")
    special_requests: str = Field(default=None, description="Any special requests for the reservation")