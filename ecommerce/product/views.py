from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Category, Brand, Product, ProductLine
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, ProductLineSerializer


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

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
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
