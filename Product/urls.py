from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'product'

urlpatterns = [
    path('registerproduct', views.ProductCreate.as_view(), name='register-product'),
]
