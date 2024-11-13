from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('list-employees', views.ListEmployee.as_view(), name='ListEmployee')
]
