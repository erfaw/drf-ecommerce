import pytest
from django.core.exceptions import ValidationError

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

    def test_ActiveQuerySet(self, product_factory):
        pass
        # TODO : make a test for ActiveQuerySet
        # queryset = product_factory.create_batch(5)
        # for q in queryset:
        #     assert q.isactive() == True


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        # Arrange
        # Act
        _unit = product_line_factory()
        # Assert
        assert _unit.__str__() == _unit.sku

    def test_duplicate_order_values(self, product_factory, product_line_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj,)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj,).clean()
