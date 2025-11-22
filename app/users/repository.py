from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.model import User


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, email: str, name: str, hashed_password: str) -> User:
    db_user = User(
        email=email,
        name=name,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_password(db: Session, user: User, hashed_password: str) -> User:
    """Update user's password."""
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return user
