import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Sneaker, Category, Brand, Base  # Замените "your_module" на фактическое имя вашего модуля, содержащего описания таблиц и классов

class TestSneakerMethods(unittest.TestCase):
    def setUp(self):
        # Создаем временную базу данных в памяти для тестов
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        
        # Создаем сессию для взаимодействия с базой данных
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Добавляем тестовые данные
        self.running_category = Category(category_name='Running')
        self.basketball_category = Category(category_name='Basketball')
        self.nike_brand = Brand(brand_name='Nike')
        self.adidas_brand = Brand(brand_name='Adidas')

        self.session.add_all([self.running_category, self.basketball_category, self.nike_brand, self.adidas_brand])
        self.session.commit()

        self.running_sneaker = Sneaker(model='Air Max', brand_id=self.nike_brand.brand_id, category_id=self.running_category.category_id, price='100.00')
        self.basketball_sneaker = Sneaker(model='Superstar', brand_id=self.adidas_brand.brand_id, category_id=self.basketball_category.category_id, price='80.00')

        self.session.add_all([self.running_sneaker, self.basketball_sneaker])
        self.session.commit()

    def tearDown(self):
        # Закрываем сессию и удаляем временную базу данных
        self.session.close()
        Base.metadata.drop_all(bind=self.engine)

    def test_get_sneaker(self):
        # Тест для метода get
        retrieved_running_sneaker = Sneaker.get(self.session, sneaker_id=self.running_sneaker.sneaker_id)
        self.assertEqual(retrieved_running_sneaker.model, 'Air Max')

        retrieved_basketball_sneaker = Sneaker.get(self.session, sneaker_id=self.basketball_sneaker.sneaker_id)
        self.assertEqual(retrieved_basketball_sneaker.model, 'Superstar')

        not_found_sneaker = Sneaker.get(self.session, sneaker_id=999)  # Несуществующий ID
        self.assertIsNone(not_found_sneaker)

    def test_find_sneaker(self):
        # Тест для метода find
        found_running_sneaker = Sneaker.find(self.session, model='Air Max')
        self.assertEqual(found_running_sneaker.model, 'Air Max')

        found_basketball_sneaker = Sneaker.find(self.session, model='Superstar')
        self.assertEqual(found_basketball_sneaker.model, 'Superstar')

        not_found_sneaker = Sneaker.find(self.session, model='NonexistentModel')
        self.assertIsNone(not_found_sneaker)

    def test_get_all_sneakers(self):
        # Тест для метода get_all
        all_sneakers = Sneaker.get_all(self.session)
        self.assertEqual(len(all_sneakers), 2)

        sneaker_models = set(sneaker.model for sneaker in all_sneakers)
        self.assertEqual(sneaker_models, {'Air Max', 'Superstar'})

    def test_delete_sneaker(self):
        # Тест для метода delete
        Sneaker.delete(self.session, sneaker_id=self.running_sneaker.sneaker_id)
        remaining_sneakers = Sneaker.get_all(self.session)
        self.assertEqual(len(remaining_sneakers), 1)

        deleted_sneaker = Sneaker.get(self.session, sneaker_id=self.running_sneaker.sneaker_id)
        self.assertIsNone(deleted_sneaker)

if __name__ == '__main__':
    unittest.main()