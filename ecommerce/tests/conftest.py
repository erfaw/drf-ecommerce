from .factories import CategoryFactory, BrandFactory, ProductFactory
from pytest_factoryboy import register

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)