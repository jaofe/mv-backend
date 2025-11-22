from pydantic import BaseModel


class SpeciesResponse(BaseModel):
    id: int
    name: str
    description: str | None

    class Config:
        from_attributes = True
