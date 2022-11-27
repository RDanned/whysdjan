import pprint

from django.db import models

# Create your models here.


class AttributeName(models.Model):
    nazev = models.TextField(null=True, blank=True)
    kod = models.TextField(null=True, blank=True)
    zobrazit = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = "Attribute name"
        verbose_name_plural = "Attribute names"


class AttributeValue(models.Model):
    hodnota = models.TextField()

    class Meta:
        verbose_name = "Attribute value"
        verbose_name_plural = "Attribute values"
        
    
class Attribute(models.Model):
    nazev_atributu_id = models.ForeignKey(AttributeName, on_delete=models.PROTECT)
    hodnota_atributu_id = models.ForeignKey(AttributeValue, on_delete=models.PROTECT)

    def __setattr__(self, attr, value):
        if attr == 'nazev_atributu_id' and type(value) is int:
            super(Attribute, self).__setattr__('nazev_atributu_id', AttributeName.objects.get(pk=value))
        elif attr == 'hodnota_atributu_id' and type(value) is int:
            super(Attribute, self).__setattr__('hodnota_atributu_id', AttributeValue.objects.get(pk=value))
        else:
            super(Attribute, self).__setattr__(attr, value)

    class Meta:
        verbose_name = "Attribute"
        verbose_name_plural = "Attributes"


class Product(models.Model):
    nazev = models.TextField()
    description = models.TextField(null=True, blank=True)
    cena = models.TextField()
    mena = models.CharField(max_length=3)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductAttributes(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __setattr__(self, attr, value):
        if attr == 'attribute' and type(value) is int:
            super(ProductAttributes, self).__setattr__('attribute', Attribute.objects.get(pk=value))
        elif attr == 'product' and type(value) is int:
            super(ProductAttributes, self).__setattr__('product', Product.objects.get(pk=value))
        else:
            super(ProductAttributes, self).__setattr__(attr, value)

    class Meta:
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"


class Image(models.Model):
    obrazek = models.TextField()
    nazev = models.TextField()

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    obrazek_id = models.ForeignKey(Image, on_delete=models.PROTECT)
    nazev = models.TextField()

    def __setattr__(self, attr, value):
        if attr == 'product' and type(value) is int:
            super(ProductImage, self).__setattr__('product', Product.objects.get(pk=value))
        elif attr == 'obrazek_id' and type(value) is int:
            super(ProductImage, self).__setattr__('obrazek_id', Image.objects.get(pk=value))
        else:
            super(ProductImage, self).__setattr__(attr, value)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class Catalog(models.Model):
    nazev = models.TextField()
    obrazek_id = models.ForeignKey(Image, on_delete=models.PROTECT)
    products_ids = models.ManyToManyField(Product)
    attributes_ids = models.ManyToManyField(Attribute)

    def __setattr__(self, attr, value):
        if attr == 'products_ids' and all(type(item) is int for item in value):
            new_val = Product.objects.filter(pk__in=value)
            self.products_ids.set(new_val)
        elif attr == 'attributes_ids' and all(type(item) is int for item in value):
            new_val = Attribute.objects.filter(pk__in=value)
            self.attributes_ids.set(new_val)
        elif attr == 'obrazek_id' and type(value) is int:
            super(Catalog, self).__setattr__('obrazek_id', Image.objects.get(pk=value))
        else:
            super(Catalog, self).__setattr__(attr, value)
