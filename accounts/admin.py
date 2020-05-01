from django.contrib import admin
from accounts.models import Org, UserProfile


allModels = [Org, UserProfile]  # iterable list
admin.site.register(allModels)
