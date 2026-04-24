# E2E test for each endpoint
import pytest

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    endpoint = r"/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange
        category_factory()
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
