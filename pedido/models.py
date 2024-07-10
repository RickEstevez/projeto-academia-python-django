from django.db import models
class Pedido(models.Model):
    Descricao = models.CharField(max_length=100)
    Valor_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Data_Pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"

    def save(self, *args, **kwargs):
        from cliente.models import Cliente
        from produto.models import Produto

        super().save(*args, **kwargs)

class ItemPedido(models.Model):
    Quantidade = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        from produto.models import Produto
        from pedido.models import Pedido

        super().save(*args, **kwargs)