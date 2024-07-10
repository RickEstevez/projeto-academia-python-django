from django.db import models
class Aula(models.Model):
    Nome = models.CharField(max_length=50)
    Horario = models.CharField(max_length=20)
    Dia = models.CharField(max_length=30)
    Serie = models.CharField(max_length=5)
    Repeticao = models.CharField(max_length=5)
    Categoria = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        from cliente.models import Cliente
        from professor.models import Professor
        from aparelho_academia.models import Aparelho_Academia
        from planos_desconto.models import Planos_Desconto

        super().save(*args, **kwargs)