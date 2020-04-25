from django.conf.urls import url, include
from payments.views import make_payment

"""
URLS FOR THE PAYMENTS APP
"""
urlpatterns = [
    url(r'^make_payment$', make_payment, name="makepayment"),
]