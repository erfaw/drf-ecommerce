from django.contrib import admin
from .models import Category, Brand, Product, ProductLine, ProductImage
from django.urls import reverse
from django.utils.safestring import mark_safe

class EditLinkInline:
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )

        if instance.pk:
            return mark_safe(f"<a href='{url}'>Edit</a>")
        else:
            return ""


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ["edit",]


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
    inlines = [ProductImageInline]

class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "url",
        "alternative_text",
        "order",
    )
    list_display_links = (
        "id",
        "name",
        "url"
    )
    list_per_page = 25

admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
