from django.contrib import admin

from . import models


admin.site.register(models.Catalog)
admin.site.register(models.Product)
admin.site.register(models.ProductAttributes)
admin.site.register(models.ProductImage)
admin.site.register(models.Image)
admin.site.register(models.AttributeName)
admin.site.register(models.AttributeValue)
admin.site.register(models.Attribute)


# Register your models here.
