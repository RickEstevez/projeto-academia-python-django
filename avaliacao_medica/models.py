from django.db import models
from cliente.models import Cliente

class Avaliacao_Medica(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Medico = models.CharField(max_length=60)
    Data_exame = models.DateField()
    Categoria_exame = models.CharField(max_length=30)
    Resultado = models.TextField()
    Atestado_medico = models.CharField(max_length=20)