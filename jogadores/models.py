from django.db import models

# Create your models here.
from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=10)
    posicao = models.CharField(max_length=13)

    def __str__(self):
        return self.nome


   