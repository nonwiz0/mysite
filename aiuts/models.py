from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class User(models.Model):
    acc_id = models.CharField(max_length=256, primary_key=True)
    password = models.CharField(max_length=256)
    balance = models.FloatField(default=0.01)
