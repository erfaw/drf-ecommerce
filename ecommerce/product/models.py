from django.db import models
from mptt.models import TreeForeignKey, MPTTModel
from .fields import OrderField
from django.core.exceptions import ValidationError


class ActiveManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_active=True)


class ActiveQuerySet(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=255,
    )
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null=False)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    # `related_name` fields
    # product_line
    objects = ActiveQuerySet.as_manager()  # objects = models.Manager()
    isactive = ActiveManager()

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # `related_name` fields
    # attribute_value
    # product_type
    

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=100)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="attribute_value"
    )
    # `related_name` fields
    # product_line_attribute_value_av
    # product_line_attribute_value


    def __str__(self):
        return f"{self.attribute}=\t{self.value}"


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, related_name="product_line_attribute_value_av")
    product_line = models.ForeignKey('ProductLine', on_delete=models.CASCADE, related_name="product_line_attribute_value_pl")

    class Meta:
        unique_together = ["attribute_value", "product_line",]
    
    def __str__(self):
        return f"{self.product_line} : {self.attribute_value}"


class ProductLine(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField() # Note: it is different than slug!
    stock_qty = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    order = OrderField(
        unique_for_field="product", blank=True
    )  # pyright: ignore[reportCallIssue]
    is_active = models.BooleanField(default=False)
    attribute_value = models.ManyToManyField(AttributeValue, through=ProductLineAttributeValue, related_name="product_line_attribute_value")
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, related_name="product_line")
    # `related_name` fields:
    # product_line_attribute_value_pl
    # product_image


    def clean(self):
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.pk != obj.pk and self.order == obj.order:
                raise ValidationError("Duplicate value .")

        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku # TODO : change return to self.name


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=r'photos/%Y/%m/%d/')
    productline = models.ForeignKey(
        ProductLine, on_delete=models.CASCADE, related_name="product_image"
    )
    order = OrderField(
        unique_for_field="productline", blank=True
    )  # pyright: ignore[reportCallIssue]

    def clean(self):
        qs = ProductImage.objects.filter(productline=self.productline)
        for obj in qs:
            if self.pk != obj.pk and self.order == obj.order:
                raise ValidationError("Duplicate value .")

        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    attribute = models.ManyToManyField(Attribute, through='ProductTypeAttribute', related_name="product_type")

    def __str__(self):
        return self.name
    # `related_name` fields
    # product_line


class ProductTypeAttribute(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name="product_type_attribute_pt")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="product_type_attribute_a")

    class Meta:
        unique_together = ["product_type", "attribute",]
    
    def __str__(self):
        return f"{self.product_type} : {self.attribute}"
    