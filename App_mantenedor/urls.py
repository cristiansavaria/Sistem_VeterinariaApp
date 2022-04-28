from django import views
from django.urls import path
from .views import index

urlpatterns = [
    path('index/', index, name='index'),
    
   
   
]