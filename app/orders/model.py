from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    total_value = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="orders")
    order_products = relationship("OrderProduct", back_populates="order")
    chats = relationship("Chat", back_populates="order")

class OrderProduct(Base):
    __tablename__ = "order_products"
    
    order_id = Column(Integer, ForeignKey("orders.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    
    # Relationships
    order = relationship("Order", back_populates="order_products")
    product = relationship("Product", back_populates="order_products")