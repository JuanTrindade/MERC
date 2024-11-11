from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('list-employees', views.ListEmployee.as_view(), name='ListEmployee')
]
