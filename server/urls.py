"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/', include('server.api.urls')),
    path('admin/', admin.site.urls),
]
