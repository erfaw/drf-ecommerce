import factory
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # Name of actual Category table model fields
    name = "test_category"
