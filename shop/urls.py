from django.urls import path
from rest_framework import routers

from shop.routes import load

app_name = 'shop'
# urlpatterns = [
#     path('import/', load.index),
#     path('send/', form.save_application),
#     path('form_data/', form.get_form_data),
# ]
router = routers.SimpleRouter()
#router.register(r'import', load.index), basename='import')

urlpatterns = [
    path('import/', load.index),
]

urlpatterns += router.urls