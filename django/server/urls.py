from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/', include('server.api.urls')),
    path('admin/', admin.site.urls),
]
