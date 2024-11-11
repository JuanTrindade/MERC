from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [ 
    path('', views.Login.as_view(), name='login'),
    path('signup', views.SignUp.as_view(), name='signup')
]
