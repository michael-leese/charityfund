"""charity_fund URL Configuration
Gets all the urls form the accounts app and all other apps
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index, logout, login, register_user, register_org, about, edit_org, view_my_orgs_appeals, change_password, edit_user_profile
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
    url(r'^accounts/change_password/$', change_password, name="changepassword"),
    url(r'^accounts/edit_user_profile/$', edit_user_profile, name="edituserprofile"),
    url(r'^email_send/', include('email_send.urls')),
]
