from rest_framework import serializers
from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = ["category_name", ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name", ]


class ProductLineSerializer(serializers.ModelSerializer):


    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['name',]


    product = ProductSerializer()

    class Meta:
        model = ProductLine
        exclude = ['id', ]


class ProductSerializer(serializers.ModelSerializer):


    class ProductLineSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProductLine
            exclude = ['id', ]


    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['id',]
