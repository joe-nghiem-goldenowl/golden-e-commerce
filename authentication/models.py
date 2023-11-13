from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(User):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = "customer"
