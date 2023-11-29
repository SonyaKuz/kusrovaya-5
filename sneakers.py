from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from tables.base import Base

class Sneaker(Base):
    __tablename__ = 'sneakers'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    price = Column(String, nullable=False)
    orders = relationship("Order", back_populates="sneaker")
    def __init__(self, brand: str, model: str, size: int, color: str, price: str):
        self.brand = brand
        self.model = model
        self.size = size
        self.color = color
        self.price = price
