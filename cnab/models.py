from django.db import models

# Create your models here.

class Upload(models.Model):
    file = models.FileField(upload_to="uploads")


class Cnab(models.Model):
    type = models.CharField(max_length=21)
    date = models.CharField(max_length=24)
    value = models.IntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=24)
    hour = models.CharField(max_length=24)
    owner = models.CharField(max_length=64)
    shop = models.CharField(max_length=64)
    