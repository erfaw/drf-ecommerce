from rest_framework import serializers
from .models import Category, Brand, Product, ProductLine, ProductImage, Attribute, AttributeValue


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = [
            "category_name",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "name",
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    productline_name = serializers.CharField(source="productline.name")

    class Meta:
        model = ProductImage
        fields = [
            "alternative_text",
            "url",
            "productline_name",
            "order",
        ]


class AttributeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Attribute
        exclude = ['id','description']


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)

    class Meta: 
        model = AttributeValue
        fields = [
            "attribute",
            "value",
        ]


class ProductLineSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = [
            "name",
            "price",
            "sku",
            "stock_qty",
            "product_name",
            "order",
            "product_image",
            "attribute_value",
        ]


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source="category.name")
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "is_digital",
            "product_line",
        ]
