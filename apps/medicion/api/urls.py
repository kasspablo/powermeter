from django.urls import path
from apps.medicion.api.api import medicion_api_view, max_view, min_view, avg_view

urlpatterns = [
    path('save',medicion_api_view, name = 'medicion_api'),
    path('get/max',max_view, name = 'maximo_api'),
    path('get/min',min_view, name = 'minimo_api'),
    path('get/avg',avg_view, name = 'promedio_api'),
]