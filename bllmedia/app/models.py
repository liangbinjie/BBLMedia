from django.db import models

# Create your models here.
class Contacto(models.Model):
    email = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.email