from django.conf.urls import url, include
from .views import do_search

"""
URLS FOR THE APPEALS APP
"""
urlpatterns = [
    url(r'^$', do_search, name="search"),
]