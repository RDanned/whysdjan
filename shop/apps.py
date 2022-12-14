from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    # Restrict models that are allowed to import
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

     # It is necessary to define the order of importing models so that there were
     # no problems with non-existent objects when importing them where they are needed
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

        # I don't want to write a handler for each model, so I did this
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

        # self.models = {
        #     'AttributeName': models.AttributeName,
        #     'AttributeValue': models.AttributeValue,
        #     'Attribute': models.Attribute,
        #     'Product': models.Product,
        #     'ProductAttributes': models.ProductAttributes,
        #     'Image': models.Image,
        #     'ProductImage': models.ProductImage,
        #     'Catalog': models.Catalog,
        # }
