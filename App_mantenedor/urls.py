from django import views
from django.urls import path
from .views import test

urlpatterns = [
    path('test/', test, name='test'),
   
   
]