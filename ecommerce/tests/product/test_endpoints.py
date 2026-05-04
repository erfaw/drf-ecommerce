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
        assert len(response.json()) == 4 # number checking
        print(response.json())


class TestBrandEndpoints:
    endpoint = r"/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200 # response checking
        assert len(response.json()) == 4 # number checking
        print(response.json())


class TestProductEndpoints:
    endpoint = r"/api/product/"

    def test_return_all_products(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200 # response checking
        assert len(response.json()) == 4 # number checking
        print(response.json())

    def test_return_single_product_by_slug(self, product_factory, api_client):
        obj = product_factory(slug="test-slug")
        response = api_client().get(f"{self.endpoint}{obj.slug}/")

        assert response.status_code == 200 

        response_json = response.json()
        if isinstance(response.json(), list,): 
            assert len(response_json) == 1
            assert response_json[0]["slug"] == obj.slug
        elif isinstance(
            response_json,dict,): 
            assert response_json["slug"] == obj.slug

    def test_return_products_by_category_slug(self, product_factory, category_factory, api_client):
        category_obj = category_factory(slug="test-category-1", name="test-category-1")
        another_category_obj = category_factory(slug="another-category-2", name="another-category-2")

        NUM_OF_RIGHT_CAT = 5
        product_obj = product_factory.create_batch(NUM_OF_RIGHT_CAT, category=category_obj,)
        another_product_obj = product_factory(category=another_category_obj)

        num_all_cats = category_obj.__class__.objects.count()
        assert num_all_cats == 2

        num_all_products = product_obj[0].__class__.objects.count()
        assert num_all_products == NUM_OF_RIGHT_CAT+1

        response_products_by_category_slug = api_client().get(f"{self.endpoint}category/{category_obj.slug}/all/")
        assert response_products_by_category_slug.status_code == 200

        response_json = response_products_by_category_slug.json()
        
        assert isinstance(response_json, list)
        assert len(response_json) == NUM_OF_RIGHT_CAT
        
        for product in response_json:
            assert product["category_name"] == category_obj.name
            assert product["category_name"] != another_category_obj.name 

class TestProductLineEndpoints:
    endpoint = r"/api/product-line/"
    
    def test_product_line_get(self, product_line_factory, api_client):
        # Arrange
        len_num = 5
        product_line_factory.create_batch(len_num)
        # Act
        response = api_client().get(self.endpoint)
        loaded_response = response.json()
        # Assert
        assert response.status_code == 200
        assert len(loaded_response) == len_num
        print(loaded_response)
