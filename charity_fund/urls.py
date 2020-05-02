"""charity_fund URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, logout, login, register_user, register_org, about, edit_org, view_my_orgs_appeals
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/about/$', about, name="about"),
    url(r'^accounts/register/$', register_user, name="register"),
    url(r'^accounts/register_org/$', register_org, name="registerorg"),
    url(r'^appeals/', include('appeals.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^payments/', include('payments.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^accounts/edit_org/$', edit_org, name="editorg"),
    url(r'^accounts/viewmyorgs_appeals/$', view_my_orgs_appeals, name="viewmyorgs_appeals"),
]
