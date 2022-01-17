from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=20, blank=False, null=False, primary_key=True)
    password=models.CharField(max_length=20,blank=False, null=False)
    mail=models.EmailField(null=False, blank=False)
    phone=models.ImageField(null=False, blank=False)

