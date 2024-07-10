from django.db import models
class Professor(models.Model):
    Nome = models.CharField(max_length=100)
    Turno = models.CharField(max_length=10)
    Email = models.EmailField()
    Telefone = models.CharField(max_length=20)
    Endereco = models.CharField(max_length=60)
    Salario = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        from cliente.models import Cliente
        from aula.models import Aula

        super().save(*args, **kwargs)