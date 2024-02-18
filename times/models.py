from django.db import models

# Create your models here.
class Time(models.Model):
    nome = models.CharField(max_length=100)
    titulos = models.CharField(max_length=30)
    fundacao = models.CharField(max_length=4)

    def __str__(self) :
        return self.nome