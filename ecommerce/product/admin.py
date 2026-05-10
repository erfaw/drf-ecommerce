from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    ProductLine,
    ProductImage,
    Attribute,
    AttributeValue,
    ProductLineAttributeValue,
    ProductType
)
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


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue.product_line_attribute_value.through # type: ignore


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
    inlines = [ProductImageInline, AttributeValueInline,]


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


class AttributeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
    )
    list_display_links = (
        "id",
        "name",
    )
    list_per_page = 25


class AttributeValueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "value",
        "attribute",
    )
    list_display_links = (
        "id",
        "value",
        "attribute",
    )
    list_per_page = 25


class ProductLineAttributeValueAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_line",
        "attribute_value__attribute",
        "attribute_value",
    )
    list_display_links = (
        "id",
    )
    list_per_page = 25


admin.site.register(ProductType,)
admin.site.register(ProductLineAttributeValue, ProductLineAttributeValueAdmin)
admin.site.register(AttributeValue, AttributeValueAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
