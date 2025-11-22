from sqlalchemy.orm import Session
from app.species.model import Species


def get_all_species(db: Session) -> list[Species]:
    return db.query(Species).order_by(Species.name).all()


def get_species_by_id(db: Session, species_id: int) -> Species | None:

    return db.query(Species).filter(Species.id == species_id).first()
