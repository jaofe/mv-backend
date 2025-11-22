from pydantic import BaseModel, Field
from datetime import datetime


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    weight: float = Field(..., gt=0)
    price: float = Field(..., gt=0)
    fishing_date: datetime
    description: str | None = Field(None, max_length=2000)
    species_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    date: datetime
    weight: float
    price: float
    location: str | None
    details: dict | None
    image_urls: list[str] | None
    status: str
    species_id: int
    user_id: int

    class Config:
        from_attributes = True
