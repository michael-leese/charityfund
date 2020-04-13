from django.db import models
from django.utils import timezone
from accounts.models import User, Org

class Appeal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    target_date = models.DateTimeField(default=timezone.now)
    money_target = models.IntegerField(null=True, blank=True)
    money_raised = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
