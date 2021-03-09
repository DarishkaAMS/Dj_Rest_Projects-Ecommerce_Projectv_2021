from django.test import TestCase

from store.models import Category, Product


class TestCategoryModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='Dummy', slug='dummy')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))


class TestProductModel(TestCase):

    def setUp(self) -> None: