import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        _unit = category_factory()
        # Assert
        # assert _unit.__str__() == "test_category"
        assert _unit.__str__() == _unit.name


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        _unit = brand_factory()
        # Assert
        assert _unit.__str__() == _unit.name


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        _unit = product_factory()
        # Assert
        assert _unit.__str__() == _unit.name


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        # Arrange
        # Act
        _unit = product_line_factory()
        # Assert
        assert _unit.__str__() == _unit.sku

    # TODO: make a test `test_duplicate_order_values` for ProductLine.clean() or clean_fields() method.
