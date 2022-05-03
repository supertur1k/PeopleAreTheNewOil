from django.db import models

# Create your models here.


class Questions(models.Model):
    worker_id = models.CharField(max_length=200, primary_key=True)
    factor = models.CharField(max_length=200)     # Показатель состояния работника
    value = models.CharField(max_length=200)      # Значение показателя
    date = models.DateTimeField('date published')
