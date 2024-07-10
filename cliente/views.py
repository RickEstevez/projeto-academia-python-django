from django.shortcuts import render
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})