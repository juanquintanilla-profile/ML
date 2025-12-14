from pydantic import BaseModel, Field
from typing import List

class LinkedinPost(BaseModel):
    title: str = Field(..., min_length=3)
    content: str = Field(..., min_length=10)
    hashtags: List[str] = Field(..., min_items=1)
    category: str = Field(..., min_length=3)

    model_config = {
        "extra": "forbid",
        "validate_assignment": True
    }
