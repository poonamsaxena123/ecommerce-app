import factory
from django.core.files.base import ContentFile
from store.models import Product, variation
from category.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    category_name = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: obj.category_name.lower())
    description = factory.Faker('sentence', nb_words=5)

    # Fake category image (optional)
    @factory.lazy_attribute
    def cat_image(self):
        return ContentFile(b'mock image data', 'test_category.jpg')



class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: obj.name.lower())
    description = factory.Faker('sentence', nb_words=3)
    price = factory.Faker('pyint', min_value=10, max_value=500)
    stock = factory.Faker('pyint', min_value=0, max_value=100)
    is_available = True
    category = factory.SubFactory(CategoryFactory)

    
    @factory.lazy_attribute
    def image(self):
        return ContentFile(b'mock image data', 'test.jpg')


class VariationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = variation

    product = factory.SubFactory(ProductFactory)
    variation_category = factory.Iterator(['color', 'size'])
    variation_value = factory.Faker('word')
    is_active = True
