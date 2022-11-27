from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
    allowed_to_import = [
        'AttributeName',
        'AttributeValue',
        'Attribute',
        'Product',
        'ProductAttributes',
        'Image',
        'ProductImage',
        'Catalog',
    ]
    models_priority = {
        'AttributeName': 1,
        'AttributeValue': 2,
        'Image': 3,
        'Attribute': 4,
        'ProductImage': 5,
        'ProductAttributes': 6,
        'Product': 7,
        'Catalog': 8,
    }
    model_serializers = {}
    models = {}

    def ready(self):
        from shop import serializers
        from shop import models

        self.model_serializers = {
            'AttributeName': serializers.AttributeNameSerializer,
            'AttributeValue': serializers.AttributeValueSerializer,
            'Attribute': serializers.AttributeSerializer,
            'Product': serializers.ProductSerializer,
            'ProductAttributes': serializers.ProductAttributesSerializer,
            'Image': serializers.ImageSerializer,
            'ProductImage': serializers.ProductImageSerializer,
            'Catalog': serializers.CatalogSerializer,
        }
