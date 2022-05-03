from django.db import models

# Create your models here.


class Questions(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    factor = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
