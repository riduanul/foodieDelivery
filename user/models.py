from django.db import models
from django.contrib.auth.models import AbstractUser

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return self.name

USER_ROLE = [
    ('Owner', 'Owner'),
    ('Employee', 'Employee'),
    ('Customer', 'Customer'),
]
class CustomUser(AbstractUser):
    role = models.CharField(choices=USER_ROLE, max_length=20, default= 'Customer')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True, blank=True)


