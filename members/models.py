from django.db import models

# Create your models here.

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Regular', 'Regular'),
)


class Member(models.Model):
    first_name = models.CharField(max_length=50, blank=False, default='')
    last_name = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=15, blank=False, default='')
    email = models.EmailField(max_length=254)
    role = models.CharField(
        max_length=8, choices=ROLE_CHOICES, default='Regular')