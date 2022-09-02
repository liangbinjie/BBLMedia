from django.db import models

# Create your models here.
class Contacto(models.Model):
    email = models.CharField(max_length=400)