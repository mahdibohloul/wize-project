from django.db import models
from django.utils import timezone


class Office(models.Model):
    office = models.CharField(max_length=256, unique=True)
    date_joined = models.DateTimeField(auto_now_add=timezone.now(), null=True)

    def __str__(self):
        return self.office


