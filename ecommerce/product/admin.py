from django.contrib import admin
from .models import Category, Brand, Product, ProductLine, ProductImage
from django.urls import reverse
from django.utils.safestring import mark_safe

class EditLinkInline:
    def edit(self, instance):
        url = reverse(f"admin:{instance._meta.app_label}_{instance._meat.model_name}_change")

        if instance.pk:
            return mark_safe(
                f"<a href='{url}'>Edit</a>"
            )
        else:
            return ""


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(admin.TabularInline):
    model = ProductLine


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
    inlines = [ProductLineInline]


class ProductLineAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "sku",
        "stock_qty",
        "product",
        "is_active",
    )
    list_filter = (
        "product",
        "is_active",
    )
    list_display_links = (
        "id",
        "name",
    )
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
