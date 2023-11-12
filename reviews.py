from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from comp.base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    sneaker_id = Column(Integer, ForeignKey('sneakers.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    review_date = Column(Date, nullable=False)

    # добавляем свойства sneaker и customer для связи с моделями Sneaker и Customer
    sneaker = relationship("Sneaker", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def __init__(self, sneaker_id: int, customer_id: int, rating: int, comment: str, review_date):
        self.sneaker_id = sneaker_id
        self.customer_id = customer_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date
