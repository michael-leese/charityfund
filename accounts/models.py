from django.db import models
from django.contrib.auth.models import User as AuthUser
from django.utils import timezone


class User(AuthUser):
    class Meta:
        proxy = True

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nickname = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.nickname

class Org(models.Model):
    REG_CHARITY = 'Registered Charity'
    COM_PRO = 'Community Project'
    ORG_TYPE_CHOICES = (
        (REG_CHARITY, 'Registered Charity'),
        (COM_PRO, 'Community Project')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    organisation = models.CharField(max_length=200)
    org_type = models.CharField(max_length=25, choices=ORG_TYPE_CHOICES, default=REG_CHARITY)
    bio = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.organisation


