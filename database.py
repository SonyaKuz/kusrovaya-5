from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base 

db_url = 'postgresql://postgres@localhost:5432/demo'

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine) 

session = SessionLocal()

# Создаем таблицы
Base.metadata.create_all(engine)

