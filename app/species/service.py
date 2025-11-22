from sqlalchemy.orm import Session
from app.species.schema import SpeciesResponse
from app.species.repository import get_all_species


def list_all_species(db: Session) -> list[SpeciesResponse]:
    species = get_all_species(db)
    return [SpeciesResponse.model_validate(s) for s in species]
