from django.db import models

# Create your models here.

class Personas(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()