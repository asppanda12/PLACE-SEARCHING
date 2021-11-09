from django import urls
from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('resturant', views.resturant, name='resturant'),
    path('police', views.police, name='police'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('tourist', views.tourist, name='tourist'),
]