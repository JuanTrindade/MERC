from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Login.urls')),
    path('home/', include('Home.urls')),
    path('acl/', include('acl.urls'))
]
