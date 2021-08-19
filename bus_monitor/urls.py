from django.urls import path

from . import views

app_name = 'bus_monitor'
urlpatterns = [
    path('', views.index, name='index'),
]
