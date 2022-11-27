from rest_framework.decorators import permission_classes, api_view
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from collections import defaultdict
from django.apps import apps
from shop import models as shop_models

import pprint


@api_view(['POST'])
@permission_classes([AllowAny])
def index(request):

    grouped_data = defaultdict(list)
    response = {}
    response.setdefault('errors', [])
    status = 200

    allowed_to_import = apps.get_app_config('shop').allowed_to_import
    model_serializers = apps.get_app_config('shop').model_serializers
    model_priority = apps.get_app_config('shop').models_priority

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

    for model_name in dict(sorted(model_priority.items(), key=lambda item: item[1])):
        grouped_data[model_name] = []

    pprint.pp(grouped_data)
    for obj in request.data:

        if len(obj.keys()) > 1:
            response['errors'].append({
                'message': 'Request contains invalid model format'
            })
            break
        else:
            model_name = list(obj.keys())[0]

        if model_name in allowed_to_import:
            grouped_data[model_name].append(obj[model_name])
        else:
            response['errors'].append({
                'model_name': model_name,
                'message': f'Request contains invalid model: {model_name}'
            })
            status = 400
            break

    for model_name in grouped_data:
        for i_f, obj_first in enumerate(grouped_data[model_name]):
            for i_s, obj_second in enumerate(grouped_data[model_name]):
                if obj_first['id'] == obj_second['id'] and i_f != i_s:
                    grouped_data[model_name][i_f] = {**obj_first, **obj_second}
                    del grouped_data[model_name][i_s]

    reordered_grouped_data = []

    for model_name in dict(sorted(model_priority.items(), key=lambda item: item[1])):
        reordered_grouped_data.append({
            'model_name': model_name,
            'items': grouped_data[model_name]
        })

    #pprint.pp(reordered_grouped_data)

    for data in reordered_grouped_data:
        for data_object in data['items']:
            tmp = model_serializers[data['model_name']](data=data_object)
            try:
                tmp.is_valid(raise_exception=True)
            except serializers.ValidationError as e:
                response['errors'].append({
                    'model_name': data['model_name'],
                    'message': e.args
                })
                status = 400
                break
            else:
                try:
                    obj = models[data['model_name']].objects.get(pk=data_object['id'])
                    for key, value in data_object.items():
                        setattr(obj, key, value)
                    obj.save()
                except models[data['model_name']].DoesNotExist:
                    obj = models[data['model_name']]()

                    for key, value in data_object.items():
                        setattr(obj, key, value)
                    obj.save()

    if status == 200:
        if not response['errors']: del response['errors']
        response['message'] = 'Import is successfully finished'
        return Response(response)
    else:
        return Response(response, status=status)


class LoadView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        pprint.pprint(request)
        return Response(True)