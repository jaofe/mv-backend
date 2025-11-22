from sqlalchemy.orm import Session
from app.products.model import Product
from datetime import datetime


def create_product(
    db: Session,
    name: str,
    weight: float,
    price: float,
    fishing_date: datetime,
    description: str | None,
    species_id: int,
    user_id: int,
    image_urls: list[str] | None = None,
    status: str = "available"
) -> Product:
    db_product = Product(
        name=name,
        description=description,
        date=fishing_date,
        weight=weight,
        price=price,
        species_id=species_id,
        user_id=user_id,
        image_urls=image_urls,
        status=status
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product_by_id(db: Session, product_id: int) -> Product | None:
    return db.query(Product).filter(Product.id == product_id).first()
