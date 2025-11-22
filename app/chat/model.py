from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Chat(Base):
    __tablename__ = "chat"
    
    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    status = Column(String, nullable=False)
    
    # Relationships
    buyer = relationship("User", foreign_keys=[buyer_id], back_populates="chats_as_buyer")
    seller = relationship("User", foreign_keys=[seller_id], back_populates="chats_as_seller")
    order = relationship("Order", back_populates="chats")
    messages = relationship("Message", back_populates="chat")
