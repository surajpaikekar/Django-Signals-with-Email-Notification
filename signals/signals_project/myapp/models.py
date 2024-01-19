from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name