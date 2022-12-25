from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TransactionInfo(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)


