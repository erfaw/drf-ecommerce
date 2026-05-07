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
from django.db.models import Prefetch

from django.db import connection
from sqlparse import format
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import SqlLexer   


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
            # self.queryset.select_related("category", "brand").get(slug=slug),
            self.queryset.select_related("category", "brand").prefetch_related(Prefetch("product_line")).prefetch_related(Prefetch("product_line__product_image")).get(slug=slug),
        )
        response = Response(serializer.data)

        print("===== (START) Query N+1 Checks =====")

        raw_sql: list[dict] = connection.queries
        print(f"Number of Executed Queries:\t{len(raw_sql)}")

        for q in raw_sql:
            print(
                highlight(
                    format(q['sql'], reindent=True),
                    SqlLexer(), 
                    TerminalFormatter(),
                )
            )
        print(f"Number of Executed Queries:\t{len(raw_sql)}")
        print("===== (END) Query N+1 Checks  =====")

        return response


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
    
    @extend_schema(responses=ProductImageSerializer)
    def list(self, request):
        """
        Get list of all ProductImages.
        """
        serializer = ProductImageSerializer(self.queryset, many=True)
        return Response(serializer.data)
