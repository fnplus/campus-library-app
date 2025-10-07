from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, HttpUrl


class Category(str, Enum):
    books = "books"
    notes = "notes"
    media = "media"
    software = "software"
    other = "other"


class ResourceBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(
        None, description="Short summary to help students decide if the resource is relevant."
    )
    category: Category
    tags: List[str] = Field(default_factory=list, description="Additional labels or course codes.")
    peer_location: HttpUrl = Field(..., description="Direct download or stream URL on the peer host.")


class ResourceCreate(ResourceBase):
    pass


class Resource(ResourceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
