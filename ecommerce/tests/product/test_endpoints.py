# E2E test for each endpoint
import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = r"/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange
        category_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200 # response checking
        assert len(json.loads(response.content)) == 4 # number checking
        print(json.loads(response.content))
