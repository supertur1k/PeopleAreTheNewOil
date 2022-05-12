from django.db import models

# Create your models here.


class Questions(models.Model):
    employee_login = models.CharField(max_length=200, default='testing')
    factor = models.CharField(max_length=200)     # Показатель состояния работника
    value = models.CharField(max_length=200)      # Значение показателя
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)


class RawQuestions(models.Model):
    employee_login = models.CharField(max_length=200, default='testing')
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
