from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String, index=True)

    sneakers = relationship("Sneaker", back_populates="brand")

    @classmethod
    def get(cls, session, brand_id):
        return session.query(cls).filter_by(brand_id=brand_id).first()

    @classmethod
    def find(cls, session, brand_name):
        return session.query(cls).filter_by(brand_name=brand_name).first()

    @classmethod
    def delete(cls, session, brand_id):
        brand = cls.get(session, brand_id)
        if brand:
            session.delete(brand)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, index=True)

    sneakers = relationship("Sneaker", back_populates="category")

    @classmethod
    def get(cls, session, category_id):
        return session.query(cls).filter_by(category_id=category_id).first()

    @classmethod
    def find(cls, session, category_name):
        return session.query(cls).filter_by(category_name=category_name).first()

    @classmethod
    def delete(cls, session, category_id):
        category = cls.get(session, category_id)
        if category:
            session.delete(category)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

class Sneaker(Base):
    __tablename__ = 'sneakers'

    sneaker_id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    brand_id = Column(Integer, ForeignKey('brands.brand_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    price = Column(String)

    brand = relationship("Brand", back_populates="sneakers")
    category = relationship("Category", back_populates="sneakers")

    @classmethod
    def get(cls, session, sneaker_id):
        return session.query(cls).filter_by(sneaker_id=sneaker_id).first()

    @classmethod
    def find(cls, session, model):
        return session.query(cls).filter_by(model=model).first()

    @classmethod
    def delete(cls, session, sneaker_id):
        sneaker = cls.get(session, sneaker_id)
        if sneaker:
            session.delete(sneaker)
            session.commit()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

