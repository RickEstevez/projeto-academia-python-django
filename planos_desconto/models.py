from django.db import models
from cliente.models import Cliente
from aula.models import Aula

class Planos_Desconto(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=100)
    Descricao = models.TextField()
    Preco = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        from cliente.models import Cliente
        from aula.models import Aula

        super().save(*args, **kwargs)