from django.conf.urls import url, include
from email_send.views import emailOrg

"""
URLS FOR THE EMAIL_SEND APP
"""
urlpatterns = [
    url(r'^emailOrg$', emailOrg, name="emailOrg"),
]