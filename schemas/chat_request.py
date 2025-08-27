from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str
    session_id: str = "64aa1b15-d131-4c24-a340-6b80bd8075d5"
