import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Base  

class TestCategoryMethods(unittest.TestCase):
    def setUp(self):
        # Создаем временную базу данных в памяти для тестов
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=self.engine)
        
        # Создаем сессию для взаимодействия с базой данных
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Добавляем тестовые данные
        self.running = Category(category_name='Running')
        self.basketball = Category(category_name='Basketball')
        self.session.add_all([self.running, self.basketball])
        self.session.commit()

    def tearDown(self):
        # Закрываем сессию и удаляем временную базу данных
        self.session.close()
        Base.metadata.drop_all(bind=self.engine)

    def test_get_category(self):
        # Тест для метода get
        retrieved_running = Category.get(self.session, category_id=self.running.category_id)
        self.assertEqual(retrieved_running.category_name, 'Running')

        retrieved_basketball = Category.get(self.session, category_id=self.basketball.category_id)
        self.assertEqual(retrieved_basketball.category_name, 'Basketball')

        not_found_category = Category.get(self.session, category_id=999)  # Несуществующий ID
        self.assertIsNone(not_found_category)

    def test_find_category(self):
        # Тест для метода find
        found_running = Category.find(self.session, category_name='Running')
        self.assertEqual(found_running.category_name, 'Running')

        found_basketball = Category.find(self.session, category_name='Basketball')
        self.assertEqual(found_basketball.category_name, 'Basketball')

        not_found_category = Category.find(self.session, category_name='NonexistentCategory')
        self.assertIsNone(not_found_category)

    def test_get_all_categories(self):
        # Тест для метода get_all
        all_categories = Category.get_all(self.session)
        self.assertEqual(len(all_categories), 2)

        category_names = set(category.category_name for category in all_categories)
        self.assertEqual(category_names, {'Running', 'Basketball'})

    def test_delete_category(self):
        # Тест для метода delete
        Category.delete(self.session, category_id=self.running.category_id)
        remaining_categories = Category.get_all(self.session)
        self.assertEqual(len(remaining_categories), 1)

        deleted_category = Category.get(self.session, category_id=self.running.category_id)
        self.assertIsNone(deleted_category)

if __name__ == '__main__':
    unittest.main()

