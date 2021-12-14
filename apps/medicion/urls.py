from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
    print('ggggggggggggggg')

app_name = "medicion_app"

urlpatterns = [
    path('medir/', DesdeApps),
    # path(
    #     '', 
    #     views.PersonasIndex.as_view(),
    #     name='index',
    # ),
    
]