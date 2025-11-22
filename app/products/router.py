from fastapi import APIRouter, Depends, File, UploadFile, Form, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.products.schema import ProductCreate, ProductResponse
from app.products.service import create_new_product
from app.users.util import get_current_user
from datetime import datetime


router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    name: str = Form(...),
    weight: float = Form(...),
    price: float = Form(...),
    fishing_date: datetime = Form(...),
    species_id: int = Form(...),
    description: str | None = Form(None),
    images: list[UploadFile] = File(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    user_id = int(current_user.get("sub"))
    
    # Create product data object
    product_data = ProductCreate(
        name=name,
        weight=weight,
        price=price,
        fishing_date=fishing_date,
        description=description,
        species_id=species_id
    )
    
    return create_new_product(db, product_data, user_id, images)
