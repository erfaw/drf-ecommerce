from rest_framework import serializers
from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductLine
        fields = "__all__"
    # TODO: test if can assign other serializer after Meta or not?
    product = ProductSerializer()

