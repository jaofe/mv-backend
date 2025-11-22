from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.users.schema import UserRegister, UserResponse, UserLogin, Token, PasswordResetRequest, PasswordReset, MessageResponse
from app.users.service import register_user, login_user, request_password_reset, reset_password


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, db: Session = Depends(get_db)):

    return register_user(db, user_data)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_data = UserLogin(email=form_data.username, password=form_data.password)
    return login_user(db, user_data)


@router.post("/password-reset-request", response_model=MessageResponse)
def password_reset_request(reset_request: PasswordResetRequest, db: Session = Depends(get_db)):

    return request_password_reset(db, reset_request)


@router.post("/password-reset", response_model=MessageResponse)
def password_reset_endpoint(reset_data: PasswordReset, db: Session = Depends(get_db)):

    return reset_password(db, reset_data)
