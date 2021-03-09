from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product


class TestCategoryModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='Dummy', slug='dummy')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    print("TestCategoryModel passed")


class TestProductModel(TestCase):

    def setUp(self) -> None:
        Product.objects.create(name='Dummy', slug='dummy')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='test title', created_by_id=1,
                                            slug='test-title', price='20.00', image='django')

        def test_product_model_entry(self):
            data = self.data1
            self.assertTrue(isinstance(data, Product))
            self.assertEqual(str(data), 'test title')

    print("TestProductModel passed")
