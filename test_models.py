import unittest
from models import Sneaker, Brand, Category

class TestSneaker(unittest.TestCase):
    def test_create_sneaker(self):
        sneaker = Sneaker(model='Test Model', brand_id=1, category_id=1, price='100.00')
        self.assertEqual(sneaker.model, 'Test Model')
        self.assertEqual(sneaker.brand_id, 1)
        self.assertEqual(sneaker.category_id, 1)
        self.assertEqual(sneaker.price, '100.00')

class TestBrand(unittest.TestCase):
    def test_create_brand(self):
        brand = Brand(brand_name='Test Brand')
        self.assertEqual(brand.brand_name, 'Test Brand')

class TestCategory(unittest.TestCase):
    def test_create_category(self):
        category = Category(category_name='Test Category')
        self.assertEqual(category.category_name, 'Test Category')

if __name__ == '__main__':
    unittest.main()