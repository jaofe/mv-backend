from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.species.schema import SpeciesResponse
from app.species.service import list_all_species
from app.users.util import get_current_user


router = APIRouter(prefix="/species", tags=["species"])


@router.get("/", response_model=list[SpeciesResponse])
def get_species(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):

    return list_all_species(db)
