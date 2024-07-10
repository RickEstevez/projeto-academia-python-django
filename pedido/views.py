from django.shortcuts import render
from .models import Pedido


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/lista_pedidos.html', {'pedidos': pedidos})


from django.shortcuts import render