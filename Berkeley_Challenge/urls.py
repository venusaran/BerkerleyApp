"""
    Berkeley_Challenge URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('berkeleyApp.api.url', 'berkeleyapp')),
    #path('admin/', admin.site.urls),
]
