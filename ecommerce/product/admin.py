from django.contrib import admin
from .models import Category, Brand, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent")
    list_filter = ("name",)
    list_display_links = (
        "id",
        "name",
    )
    list_per_page = 25


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    list_display_links = (
        "id",
        "name",
    )
    list_per_page = 25


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    list_display_links = (
        "id",
        "name",
    )
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
