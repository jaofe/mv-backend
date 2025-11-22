from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Message(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chat.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(String, nullable=False)
    
    # Relationships
    chat = relationship("Chat", back_populates="messages")
    user = relationship("User", back_populates="messages")
