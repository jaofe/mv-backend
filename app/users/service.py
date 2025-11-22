from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.users.schema import UserRegister, UserResponse
from app.users.repository import get_user_by_email, create_user
from app.users.util import hash_password


def register_user(db: Session, user_data: UserRegister) -> UserResponse:
    # Check if user already exists
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = hash_password(user_data.password)
    
    new_user = create_user(
        db=db,
        email=user_data.email,
        name=user_data.name,
        hashed_password=hashed_password
    )
    
    return UserResponse.model_validate(new_user)
