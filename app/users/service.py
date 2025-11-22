from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.users.schema import UserRegister, UserResponse, UserLogin, Token, PasswordResetRequest, PasswordReset, MessageResponse
from app.users.repository import get_user_by_email, create_user, update_user_password
from app.users.util import hash_password, verify_password, create_access_token, create_password_reset_token, verify_password_reset_token
from app.mail.service import send_email


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


def request_password_reset(db: Session, reset_request: PasswordResetRequest) -> MessageResponse:
    # Check if user exists
    user = get_user_by_email(db, reset_request.email)
    
    # Always return success message for security (don't reveal if email exists), but only send email if user actually exists
    if user:
        # Generate password reset token
        reset_token = create_password_reset_token(user.email)
        
        # Create email message
        subject = "Password Reset Request"
        message = f"""
Olá {user.name},

Você solicitou a redefinição da sua senha. Utilize o seguinte token para realizar a alteração:

{reset_token}

Este token irá expirar em 15 minutos.

Se você não solicitou a redefinição de senha, por favor, ignore este e-mail.

Atenciosamente,
Equipe Maré Viva
        """
        
        # Send email
        try:
            send_email(
                recipient=user.email,
                subject=subject,
                message=message
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to send reset email. Please try again later."
            )
    
    return MessageResponse(message="If the email exists, a password reset link has been sent.")


def reset_password(db: Session, reset_data: PasswordReset) -> MessageResponse:
    # Verify the reset token
    email = verify_password_reset_token(reset_data.token)
    
    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired reset token"
        )
    
    # Get user by email
    user = get_user_by_email(db, email)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Hash the new password
    hashed_password = hash_password(reset_data.new_password)
    
    # Update user password
    update_user_password(db, user, hashed_password)
    
    return MessageResponse(message="Password has been reset successfully")
