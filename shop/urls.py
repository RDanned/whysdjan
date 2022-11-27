from django.urls import path
from rest_framework import routers

from shop.routes import load
from shop.routes import model

app_name = 'shop'
router = routers.SimpleRouter()

urlpatterns = [
    path('import/', load.index),
    path('detail/<str:model_name>/', model.list),
    path('detail/<str:model_name>/<int:obj_id>', model.detail),
]

urlpatterns += router.urls