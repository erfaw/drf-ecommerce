import factory
from ecommerce.product.models import Brand, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # Name of actual Category table model fields
    name = "test_category"


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    # Name of actual Category table model fields
    name = "test_brand"
