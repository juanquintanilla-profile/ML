from pydantic import BaseModel, Field, field_validator
from typing import List

class LinkedinPost(BaseModel):
    title: str = Field(..., min_length=3)
    content: str = Field(..., min_length=10)
    hashtags: List[str] = Field(..., min_items=1)
    category: str = Field(..., min_length=3)

    @field_validator("hashtags")
    def validate_hashtags(cls, v):
        for tag in v:
            if " " in tag or not tag.startswith("#"):
                raise ValueError("Cada hashtag debe empezar por # y no contener espacios.")
        return v

    model_config = {
        "extra": "forbid",
        "validate_assignment": True
    }
