from django.db import models
from django.utils import timezone
from accounts.models import User, Org
from taggit.managers import TaggableManager

class Appeal(models.Model):
    '''
    Appeals model
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    target_date = models.DateTimeField(default=timezone.now)
    money_target = models.IntegerField(null=True, blank=True)
    money_raised = models.IntegerField(default=0)
    tags = TaggableManager()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)

    def __str__(self):
        return self.title
