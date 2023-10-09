"""Module providing classes for schemas"""
from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    """Class representing the input request"""
    prompt: str = Field(min_length=5, max_length=50)
