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


class TestBrandEndpoints:
    endpoint = r"/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200 # response checking
        assert len(json.loads(response.content)) == 4 # number checking
        print(json.loads(response.content))


class TestProductEndpoints:
    endpoint = r"/api/product/"

    def test_return_all_products(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200 # response checking
        assert len(json.loads(response.content)) == 4 # number checking
        print(json.loads(response.content))


class TestProductLineEndpoints:
    endpoint = r"/api/product-line/"
    
    def test_product_line_get(self, product_line_factory, api_client):
        # Arrange
        len_num = 5
        product_line_factory.create_batch(len_num)
        # Act
        response = api_client().get(self.endpoint)
        loaded_response = json.loads(response.content)
        # Assert
        assert response.status_code == 200
        assert len(loaded_response) == len_num
        print(loaded_response)
