from django.urls import path
from django.conf.urls import include
from . import views
urlpatterns = [
    path('', views.cancion_list, name='cancion_list'),
]
