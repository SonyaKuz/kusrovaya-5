from sqlalchemy import Column, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from tables.base import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    sneaker_id = Column(Integer, ForeignKey('sneakers.id'), nullable=False)
    order_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

     # добавляем свойства customer и sneaker для связи с моделями Customer и Sneaker
    customer = relationship("Customer", back_populates="orders")
    sneaker = relationship("Sneaker", back_populates="orders")

    def __init__(self, customer_id: int, sneaker_id: int, order_date, quantity: int, total_price: float):
        self.customer_id = customer_id
        self.sneaker_id = sneaker_id
        self.order_date = order_date
        self.quantity = quantity
        self.total_price = total_price
