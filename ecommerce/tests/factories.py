import factory
from factory.declarations import SubFactory, Sequence 
from ecommerce.product.models import (
    Brand,
    Category,
    Product,
    ProductLine,
    ProductImage,
    Attribute,
    ProductType,
)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Sequence(lambda n: f"category-{n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = Sequence(lambda n: f"brand-{n}")


class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = Sequence(lambda num: f"attribute-test-{num}")
    description = "descriptino-test"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductType

    name = Sequence(lambda num: f"product-type-test-{num}")
    # attribute = SubFactory(AttributeFactory)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Sequence(lambda n: f"product-{n}")
    description = Sequence(lambda n: f"test_description-{n}")
    is_digital = True
    brand = SubFactory(BrandFactory)
    category = SubFactory(CategoryFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductLine

    name = Sequence(lambda n: f"ProductLine-{n}")
    price = 999.10
    sku = "test-sku"
    stock_qty = 123456789
    product = SubFactory(ProductFactory)
    is_active = True
    # Why there is not any 'order' ==> because its generate automaticly


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductImage

    name = Sequence(lambda n: f"ProductImage-{n}")
    alternative_text = "alternative_text-test"
    url = "https://url-test.com"
    productline = SubFactory(ProductLineFactory)
    # Why there is not any 'order' ==> because its generate automaticly
