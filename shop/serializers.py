import pprint
from rest_framework import serializers
from shop import models

# Mixin for extra fields checking
class ExtraFieldsMixin:

    # Raise an error if extra fields were provided
    def is_valid(self, raise_exception=False):
        if hasattr(self, 'initial_data'):
            payload_keys = self.initial_data.keys()  # all the payload keys
            serializer_fields = self.fields.keys()  # all the serializer fields
            extra_fields = list(filter(lambda key: key not in serializer_fields, payload_keys))
            if extra_fields:
                raise serializers.ValidationError('Extra fields %s in payload' % str(extra_fields))
        return super().is_valid(raise_exception=raise_exception)


class AttributeNameSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    nazev = serializers.CharField(allow_null=True, required=False)
    kod = serializers.CharField(allow_null=True, required=False)
    zobrazit = serializers.BooleanField(allow_null=True, required=False)

    class Meta:
        model = models.AttributeName
        fields = ['id', 'nazev', 'kod', 'zobrazit']


class AttributeValueSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    hodnota = serializers.CharField()

    class Meta:
        model = models.AttributeValue
        fields = ['id', 'hodnota']


class AttributeSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    nazev_atributu_id = serializers.PrimaryKeyRelatedField(queryset=models.AttributeName.objects.all())
    hodnota_atributu_id = serializers.PrimaryKeyRelatedField(queryset=models.AttributeValue.objects.all())

    class Meta:
        model = models.Attribute
        fields = ['id', 'nazev_atributu_id', 'hodnota_atributu_id']


class ProductSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    nazev = serializers.CharField()
    description = serializers.CharField(required=False)
    cena = serializers.CharField()
    mena = serializers.CharField(max_length=3)
    published_on = serializers.DateTimeField(allow_null=True, required=False)
    is_published = serializers.BooleanField(default=False)

    class Meta:
        model = models.Product
        fields = ['id', 'nazev', 'description', 'cena', 'mena', 'published_on', 'is_published']


class ProductAttributesSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=models.Attribute.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())

    class Meta:
        model = models.ProductAttributes
        fields = ['id', 'attribute', 'product']


class ImageSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    obrazek = serializers.CharField()
    nazev = serializers.CharField(required=False)

    class Meta:
        model = models.Image
        fields = ['id', 'obrazek', 'nazev']


class ProductImageSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all())
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=models.Image.objects.all())
    nazev = serializers.CharField()

    class Meta:
        model = models.ProductImage
        fields = ['id', 'product', 'obrazek_id', 'nazev']


class CatalogSerializer(ExtraFieldsMixin, serializers.ModelSerializer):
    nazev = serializers.CharField()
    obrazek_id = serializers.PrimaryKeyRelatedField(queryset=models.Image.objects.all())
    products_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Product.objects.all())
    attributes_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Attribute.objects.all())

    class Meta:
        model = models.Catalog
        fields = ['id', 'nazev', 'obrazek_id', 'products_ids', 'attributes_ids']