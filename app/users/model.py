from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=True)
    phone_number = Column(String, nullable=True)
    is_certified = Column(Boolean, default=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    # Relationships
    products = relationship("Product", back_populates="user")
    orders = relationship("Order", back_populates="user")
    chats_as_buyer = relationship("Chat", foreign_keys="Chat.buyer_id", back_populates="buyer")
    chats_as_seller = relationship("Chat", foreign_keys="Chat.seller_id", back_populates="seller")
    messages = relationship("Message", back_populates="user")
