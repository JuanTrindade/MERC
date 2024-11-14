from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'acl'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('registerclient', views.RegisterClient.as_view(), name='register-client'),
    path('registersupplier', views.RegisterSupplier.as_view(), name='register-supplier')
]