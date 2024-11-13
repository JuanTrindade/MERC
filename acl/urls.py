from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'acl'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('signclient', views.SignClient.as_view(), name='signclient'),
    path('signsupplier', views.SignSupplier.as_view(), name='signsupplier')
]