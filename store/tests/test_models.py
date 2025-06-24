from django.test import TestCase
from store.factories import ProductFactory, VariationFactory

class ProductModelTest(TestCase):

    def test_create_product(self):
        product = ProductFactory()
        self.assertIsNotNone(product.id)
        self.assertIsNotNone(product.category)
        self.assertTrue(product.image)

    def test_is_in_stock_true(self):
        product = ProductFactory(stock=10)
        self.assertTrue(product.is_in_stock())

    def test_is_in_stock_false(self):
        product = ProductFactory(stock=0)
        self.assertFalse(product.is_in_stock())

class VariationModelTest(TestCase):

    def test_create_variation(self):
        variation = VariationFactory()
        self.assertIsNotNone(variation.id)
        self.assertIsNotNone(variation.product)
        self.assertIn(variation.variation_category, ['color', 'size'])
