# tag model
from pydantic import BaseModel, Field


class Tag(BaseModel):
    name: str = Field(regex="^[a-z_]{3,15}$",
                      description="The tag name should be a string that conforms to [a-z_]{3,15}")
    value: int = Field(0, ge=0, lt=10,
                       description="The value can be any positive integer (less than 10)")
