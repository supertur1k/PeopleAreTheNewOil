from django.db import models

# Create your models here.


class Questions(models.Model):
    employee_login = models.CharField(max_length=200, default='testing')
    condition = models.CharField(max_length=200)  # Оценка состояния здоровья работника по результатам теста
    month = models.IntegerField()
    year = models.IntegerField()


class RawQuestions(models.Model):
    employee_login = models.CharField(max_length=200, default='testing')
    question = models.IntegerField()
    answer = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
