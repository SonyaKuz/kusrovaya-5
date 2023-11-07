from sqlalchemy import Column, Integer, String
from comp.base import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)

    def __init__(self, name: str, email: str, phone_number: str, address: str):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
