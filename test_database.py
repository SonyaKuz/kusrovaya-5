import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

class TestDatabase(unittest.TestCase):
    def test_database_connection(self):
        # Задаем URL вашей тестовой базы данных
        db_url = 'postgresql://postgres:123@localhost:5432/testbd1'  # Обратите внимание, что добавлен суффикс _test

        # Создаем движок для подключения к базе данных
        engine = create_engine(db_url)

        # Проверяем успешность подключения к базе данных
        connection = engine.connect()
        self.assertIsNotNone(connection)
        connection.close()

    def test_create_session(self):
        # Задаем URL вашей тестовой базы данных
        db_url = 'postgresql://postgres:123@localhost:5432/testbd1_test'  # Обратите внимание, что добавлен суффикс _test

        # Создаем движок для подключения к базе данных
        engine = create_engine(db_url)

        # Создаем сессию для взаимодействия с базой данных
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()

        # Проверяем успешность создания сессии
        self.assertIsNotNone(session)
        session.close()

if __name__ == '__main__':
    unittest.main()

