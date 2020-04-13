from django.conf.urls import url, include
from django.contrib import admin
from .views import create_appeal

urlpatterns = [
    url(r'^create_appeal/$', create_appeal, name="createappeal"),
]