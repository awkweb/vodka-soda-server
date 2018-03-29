"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from server.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'locations', views.UserLocationViewSet)
router.register(r'photos', views.UserPhotoViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^v1/auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^v1/auth-api/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
