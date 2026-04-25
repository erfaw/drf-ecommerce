import factory
from ecommerce.product.models import Brand, Category, Product, ProductLine


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name =  factory.Sequence(lambda n: f"category-{n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f"brand-{n}")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"product-{n}")
    description = factory.Sequence(lambda n: f"test_description-{n}")
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductLine

    name = factory.Sequence(lambda n: f"ProductLine-{n}")
    price = 999.10
    sku = "test-sku"
    stock_qty = 123456789
    product = factory.SubFactory(ProductFactory)
    is_active = True