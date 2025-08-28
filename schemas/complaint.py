from pydantic import BaseModel, Field


class Complaint(BaseModel):
    """Represents a customer complaint."""
    name: str = Field(default=None, description="The user's full name. Validate that the name contains only letters and spaces and the full name is given, if not prompt the user to provide the correct name")
    contact_number: str = Field(default=None, description="Contact information ex: +94712578293 (should include country code if not included, assume +94)")
    complaint_details: str = Field(..., description="The details of the complaint.")