from django.db import models
class Produto(models.Model):
    Nome = models.CharField(max_length=100)
    Descricao = models.TextField()
    Preco = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        from pedido.models import Pedido

        super().save(*args, **kwargs)