from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhoneNumber(models.Model):
    name = models.CharField(max_length = 150)
    address = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.phone_number} | {self.address} | {self.phone_number}'
