from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=32)
    phone_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000000)])

#python3 manage.py makemigrations
#python3 manage.py migrate 