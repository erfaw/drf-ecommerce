import factory
from factory.declarations import SubFactory, Sequence
from factory.helpers import post_generation
from ecommerce.product.models import (
    Brand,
    Category,
    Product,
    ProductLine,
    ProductImage,
    Attribute,
    ProductType,
    AttributeValue,
)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Sequence(lambda n: f"category-{n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = Sequence(lambda n: f"brand-{n}")


class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = Sequence(lambda num: f"attribute-test-{num}")
    description = "descriptino-test"


class AttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = AttributeValue
    
    value = "attr_test-"
    attribute = SubFactory(AttributeFactory)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductType
        skip_postgeneration_save = True

    name = Sequence(lambda num: f"product-type-test-{num}")
    
    @post_generation
    def attribute(self, create, extracted, **kwargs):
        if not create or not extracted:
            return 
        self.attribute.add(*extracted) # type: ignore
        self.save() # type: ignore

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Sequence(lambda n: f"product-{n}")
    description = Sequence(lambda n: f"test_description-{n}")
    is_digital = True
    brand = SubFactory(BrandFactory)
    category = SubFactory(CategoryFactory)
    is_active = True
    product_type = SubFactory(ProductTypeFactory)


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductLine
        skip_postgeneration_save = True

    name = Sequence(lambda n: f"ProductLine-{n}")
    price = 999.10
    sku = "test-sku"
    stock_qty = 123456789
    product = SubFactory(ProductFactory)
    is_active = True
    # Why there is not any 'order' ==> because its generate automaticly
    
    @post_generation
    def attribute_value(self, create, extracted, **kwargs):
        if not create or not extracted:
            return 
        self.attribute_value.add(*extracted) # type: ignore
        self.save() # type: ignore


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = ProductImage

    name = Sequence(lambda n: f"ProductImage-{n}")
    alternative_text = "alternative_text-test"
    url = "https://url-test.com"
    productline = SubFactory(ProductLineFactory)
    # Why there is not any 'order' ==> because its generate automaticly
