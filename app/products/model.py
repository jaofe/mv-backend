from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    date = Column(DateTime, nullable=False)
    weight = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    location = Column(Text, nullable=False)
    details = Column(JSONB)
    image_urls = Column(JSONB)
    status = Column(String, nullable=False)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationships
    species = relationship("Species", back_populates="products")
    user = relationship("User", back_populates="products")
    order_products = relationship("OrderProduct", back_populates="product")
