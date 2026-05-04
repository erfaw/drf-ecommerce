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

    def test_ActiveQuerySet(self, product_factory, product_line_factory):
        """
        Make a Product then make few ProductLine which is_active=True and assign to Product, then make just one is_active=False ProductLine and assign, then assert to test all this situation and also **Product.objects.isactive()**
        """
        product_test_record = product_factory()
        TRUE_NUM = 5

        true_product_lines = product_line_factory.create_batch(
            TRUE_NUM,
            product=product_test_record,
        )

        false_product_line_test_record =product_line_factory(
            product=product_test_record,
            name="is_active=false-1",
            is_active=False,
        )

        assert false_product_line_test_record.is_active == False
        
        assert len(true_product_lines) == TRUE_NUM

        num_all_product_lines = true_product_lines[0].__class__.objects.count()
        assert num_all_product_lines == TRUE_NUM+1

        last_product_line_by_query = true_product_lines[0].__class__.objects.latest('id')
        assert last_product_line_by_query.is_active == False

        qs = product_test_record.__class__.objects.isactive()
        for pl in qs:
            assert pl.is_active == True


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
