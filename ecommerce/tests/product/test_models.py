class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        _unit = category_factory()
        # Assert
        assert _unit.__str__() == "test_factory"


class TestBrandModel:
    def test_str_method(self):
        # Arrange
        # Act
        # Assert
        pass


class TestProductModel:
    def test_str_method(self):
        # Arrange
        # Act
        # Assert
        pass
