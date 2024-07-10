from django.db import models
from aula.models import Aula

class Aparelho_Academia(models.Model):
    Aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=60)
