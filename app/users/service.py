from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.users.schema import UserRegister, UserResponse, UserLogin, Token
from app.users.repository import get_user_by_email, create_user
from app.users.util import hash_password, verify_password, create_access_token


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


def login_user(db: Session, user_data: UserLogin) -> Token:
    user = get_user_by_email(db, user_data.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": str(user.id), "email": user.email})
    
    return Token(access_token=access_token)
