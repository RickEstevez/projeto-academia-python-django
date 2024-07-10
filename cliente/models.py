from django.db import models
class Cliente(models.Model):
    CPF = models.CharField(max_length=14)
    Nome = models.CharField(max_length=100)
    Email = models.EmailField()
    Telefone = models.CharField(max_length=20)
    Endereco = models.CharField(max_length=60)

    def save(self, *args, **kwargs):
        from aula.models import Aula
        from professor.models import Professor
        from avaliacao_medica.models import Avaliacao_Medica
        from planos_desconto.models import Planos_Desconto
        from pedido.models import Pedido


        super().save(*args, **kwargs)