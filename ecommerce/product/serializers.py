from rest_framework import serializers
from .models import Category, Brand, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", ]


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


    brand = BrandSerializer()
    category = CategorySerializer()
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['id',]
