from sqlalchemy.orm import Session
from app.species.model import Species


def get_all_species(db: Session) -> list[Species]:
    return db.query(Species).order_by(Species.name).all()
