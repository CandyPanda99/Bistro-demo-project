from pydantic import BaseModel, Field


class Complaint(BaseModel):
    """Represents a customer complaint."""
    name: str = Field(default=None, description="The user's full name.")
    contact_number: str = Field(default=None, description="Contact information ex: 0712578293")
    complaint_details: str = Field(..., description="The details of the complaint.")