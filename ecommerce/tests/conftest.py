from .factories import (
    CategoryFactory,
    BrandFactory, 
    ProductFactory, 
    ProductLineFactory
    )
from pytest_factoryboy import register
from rest_framework.test import APIClient
import pytest

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)


@pytest.fixture
def api_client():
    return APIClient
