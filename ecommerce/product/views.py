from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product, ProductLine, ProductImage
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
    ProductLineSerializer,
    ProductImageSerializer
)


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing all categories.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    a simple ViewSet for viewing all brands.
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    a simple ViewSet for viewing all products.
    """

    queryset = Product.isactive.all()
    lookup_field = "slug"

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    @action(
        methods=['GET'],
        detail=False,
        url_path=r"category/(?P<slug>[\w-]+)/all", # must be without end slash!
    )
    def list_by_category_slug(self, request, slug=None):
        """
        an endpoint to get products by category slug.
        """
        serializer = ProductSerializer(
            self.queryset.filter(category__slug=slug),
            many=True,
        )
        return Response(serializer.data)
    
    @extend_schema(responses=ProductSerializer)
    def retrieve(self, request, slug=None):
        """
        to get a single product by slug
        """
        serializer = ProductSerializer(
            self.queryset.select_related("category", "brand").get(slug=slug),
        )
        return Response(serializer.data)


class ProductLineViewSet(viewsets.ViewSet):
    """
    a simple ViewSet to get all ProductLines.
    """

    queryset = ProductLine.objects.all()

    @extend_schema(responses=ProductLineSerializer)
    def list(self, request):
        serializer = ProductLineSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductImageViewSet(viewsets.ViewSet):
    """
    A ViewSet to work with ProductImage Model.
    """
    queryset = ProductImage.objects.all()

    def list(self):
        """
        Get list of all ProductImages.
        """
        serializer = ProductImageSerializer(self.queryset, many=True)
        return Response(serializer.data)
