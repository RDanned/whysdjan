from rest_framework import serializers
from . import models

class AttributeNameSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField(allow_null=True, required=False)
    kod = serializers.CharField(allow_null=True, required=False)
    zobrazit = serializers.BooleanField(allow_null=True, required=False)

    class Meta:
        model = models.AttributeName
        fields = ['id', 'nazev', 'kod', 'zobrazit']


class AttributeValueSerializer(serializers.ModelSerializer):
    hodnota = serializers.CharField()

    class Meta:
        model = models.AttributeValue
        fields = ['id', 'hodnota']


class AttributeSerializer(serializers.ModelSerializer):
    nazev_atributu_id = serializers.PrimaryKeyRelatedField(queryset=models.AttributeName.objects.all())
    hodnota_atributu_id = serializers.PrimaryKeyRelatedField(queryset=models.AttributeValue.objects.all())

    class Meta:
        model = models.Attribute
        fields = ['id', 'nazev_atributu_id', 'hodnota_atributu_id']


class ProductSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField()
    description = serializers.CharField(required=False)
    cena = serializers.CharField()
    mena = serializers.CharField(max_length=3)
    published_on = serializers.DateTimeField(allow_null=True, required=False)
    is_published = serializers.BooleanField(default=False)

    class Meta:
        model = models.Product
        fields = ['id', 'nazev', 'description', 'cena', 'mena', 'published_on', 'is_published']


class ProductAttributesSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=models.Attribute.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())

    class Meta:
        model = models.ProductAttributes
        fields = ['id', 'attribute', 'product']


class ImageSerializer(serializers.ModelSerializer):
    obrazek = serializers.CharField()
    nazev = serializers.CharField(required=False)

    class Meta:
        model = models.Image
        fields = ['id', 'obrazek', 'nazev']


class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=models.Image.objects.all())
    nazev = serializers.CharField()

    class Meta:
        model = models.ProductImage
        fields = ['id', 'product', 'obrazek_id', 'nazev']


class CatalogSerializer(serializers.ModelSerializer):
    nazev = serializers.CharField()
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=models.Image.objects.all())
    products_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Product.objects.all())
    attributes_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Attribute.objects.all())

    class Meta:
        model = models.Catalog
        fields = ['id', 'nazev', 'obrazek_id', 'products_ids', 'attributes_ids']