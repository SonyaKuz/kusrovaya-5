import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Brand, Base

class TestBrandMethods(unittest.TestCase):
   def setUp(self):
        # Создаем временную базу данных в памяти для тестов
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        
        # Создаем сессию для взаимодействия с базой данных
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Добавляем тестовые данные
        self.nike = Brand(brand_name='Nike')
        self.adidas = Brand(brand_name='Adidas')
        self.session.add_all([self.nike, self.adidas])
        self.session.commit()

   def tearDown(self):
        # Закрываем сессию и удаляем временную базу данных
        self.session.close()
        Base.metadata.drop_all(bind=self.engine)

   def test_get_brand(self):
        # Тест для метода get
        retrieved_nike = Brand.get(self.session, brand_id=self.nike.brand_id)
        self.assertEqual(retrieved_nike.brand_name, 'Nike')

        retrieved_adidas = Brand.get(self.session, brand_id=self.adidas.brand_id)
        self.assertEqual(retrieved_adidas.brand_name, 'Adidas')

        not_found_brand = Brand.get(self.session, brand_id=999)  # Несуществующий ID
        self.assertIsNone(not_found_brand)

   def test_find_brand(self):
        # Тест для метода find
        found_nike = Brand.find(self.session, brand_name='Nike')
        self.assertEqual(found_nike.brand_name, 'Nike')

        found_adidas = Brand.find(self.session, brand_name='Adidas')
        self.assertEqual(found_adidas.brand_name, 'Adidas')

        not_found_brand = Brand.find(self.session, brand_name='NonexistentBrand')
        self.assertIsNone(not_found_brand)

   def test_get_all_brands(self):
        # Тест для метода get_all
        all_brands = Brand.get_all(self.session)
        self.assertEqual(len(all_brands), 2)

        brand_names = set(brand.brand_name for brand in all_brands)
        self.assertEqual(brand_names, {'Nike', 'Adidas'})

   def test_delete_brand(self):
        # Тест для метода delete
        Brand.delete(self.session, brand_id=self.nike.brand_id)
        remaining_brands = Brand.get_all(self.session)
        self.assertEqual(len(remaining_brands), 1)

        deleted_brand = Brand.get(self.session, brand_id=self.nike.brand_id)
        self.assertIsNone(deleted_brand)

if __name__ == '__main__':
    unittest.main()