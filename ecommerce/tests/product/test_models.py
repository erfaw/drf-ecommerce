import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        _unit = category_factory()
        # Assert
        assert _unit.__str__() == "test_category"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        _unit = brand_factory()
        # Assert
        assert _unit.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        _unit = product_factory()
        # Assert
        assert _unit.__str__() == "test_product"