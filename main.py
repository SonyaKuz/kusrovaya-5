from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Brand, Category, Sneaker

db_url = 'postgresql://postgres@localhost:5432/demo'

engine = create_engine(db_url)

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
db_session = SessionLocal()

# Пример создания нового бренда
new_brand = Brand(brand_name='Nike')
db_session.add(new_brand)
db_session.commit()

# Пример создания новой категории
new_category = Category(category_name='Running')
db_session.add(new_category)
db_session.commit()

# Пример создания новой кроссовки
new_sneaker = Sneaker(model='Air Max', brand_id=new_brand.brand_id, category_id=new_category.category_id, price='150.00')
db_session.add(new_sneaker)
db_session.commit()

# Вывод информации
print("Созданный бренд:", Brand.get(db_session, new_brand.brand_id))
print("Созданная категория:", Category.get(db_session, new_category.category_id))
print("Созданные кроссовки:", Sneaker.get(db_session, new_sneaker.sneaker_id))

db_session.close()
