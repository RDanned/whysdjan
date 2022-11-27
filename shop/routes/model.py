from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from shop import models as shop_models
from django.apps import apps

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list(request, model_name):
    model_serializers = apps.get_app_config('shop').model_serializers
    models = {
        'AttributeName': shop_models.AttributeName,
        'AttributeValue': shop_models.AttributeValue,
        'Attribute': shop_models.Attribute,
        'Product': shop_models.Product,
        'ProductAttributes': shop_models.ProductAttributes,
        'Image': shop_models.Image,
        'ProductImage': shop_models.ProductImage,
        'Catalog': shop_models.Catalog,
    }

    response = {}
    response.setdefault('errors', [])
    status = 200

    if model_name not in models:
        response['errors'].append(f'Invalid model: {model_name}')
        status = 400

    if status == 200:
        if not response['errors']: del response['errors']
        objs = models[model_name].objects.all()
        response['items'] = model_serializers[model_name](objs, many=True).data
        response['total'] = objs.count()
        return Response(response)
    else:
        return Response(response, status)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def detail(request, model_name, obj_id):
    model_serializers = apps.get_app_config('shop').model_serializers
    models = {
        'AttributeName': shop_models.AttributeName,
        'AttributeValue': shop_models.AttributeValue,
        'Attribute': shop_models.Attribute,
        'Product': shop_models.Product,
        'ProductAttributes': shop_models.ProductAttributes,
        'Image': shop_models.Image,
        'ProductImage': shop_models.ProductImage,
        'Catalog': shop_models.Catalog,
    }

    response = {}
    response.setdefault('errors', [])
    status = 200

    if model_name not in models:
        response['errors'].append(f'Invalid model: {model_name}')
        
    try:
        obj = models[model_name].objects.get(pk=obj_id)
    except models[model_name].DoesNotExist as e:
        response['errors'].append(f'Object does not exists: {model_name}: {obj_id}')
        status = 400
    else:
        response['item'] = model_serializers[model_name](obj).data

    if not response['errors']: del response['errors']
    return Response(response, status)
