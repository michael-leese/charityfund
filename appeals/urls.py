from django.conf.urls import url, include
from django.contrib import admin
from .views import create_appeal, show_all_appeals, single_appeal

"""
URLS FOR THE APPEALS APP
"""
urlpatterns = [
    url(r'^create_appeal/$', create_appeal, name="createappeal"),
    url(r'^show_all_appeals/$', show_all_appeals, name="showallappeals"),
    url(r'^single_appeal/$', single_appeal, name="singleappeal"),
]