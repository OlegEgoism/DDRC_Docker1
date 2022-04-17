from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField('Имя', max_length=250, unique=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    streat = models.CharField('Улица', max_length=50)
    number = models.IntegerField('Номер дома')

    def __str__(self):
        return self.streat