from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Product,
    ProductLine,
    ProductImage,
    Attribute,
    AttributeValue,
    ProductType,
)


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
    attribute_value = AttributeValueSerializer(many=True)

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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop('attribute_value')
        
        attr_value = {}
        for key in av_data:
            attr_value.update({
                key['attribute']['name']: key['value']
            })

        data.update({
            'specification': attr_value
        })

        return data


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
    
    def to_representation(self, instance):
        data:dict = super().to_representation(instance)

        # TODO: Make it like 'ProductLineSerializer.to_representation()'

        return data

class ProductTypeSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=True)
    product = ProductSerializer(many=True)

    class Meta:
        model = ProductType
        fields = "__all__"
