from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'product'

urlpatterns = [
    path('registerproduct', views.ProductCreate.as_view(), name='register-product'),
    path('listproduct', views.ProductList.as_view(), name='list-product'),
    path('<int:pk>/updateproduct', views.ProductUpdate.as_view(), name='update-product'),
    path('<int:pk>/deleteproduct', views.ProductDelete.as_view(), name='delete-product'),

    path('listsell', views.ProductSellList.as_view(), name='list-sell'),
    path('<int:pk>/sellproduct', views.ProductSell.as_view(), name='sell-product'),
]
