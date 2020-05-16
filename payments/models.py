from django.db import models
from django.utils import timezone
from appeals.models import Appeal
from accounts.models import User, Org

# Order model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    org = models.ForeignKey(Org, on_delete=models.DO_NOTHING)
    appeal = models.ForeignKey(Appeal, on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=100, blank=False)
    street_address1 = models.CharField(max_length=100, blank=False)
    street_address2 = models.CharField(max_length=100, blank=True)
    town_or_city = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=100, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(null=True, blank=True)
    anonymous = models.BooleanField(default=False)
    successful = models.BooleanField(default=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.created_date, self.full_name)
