from django.shortcuts import render
from .models import Planos_Desconto

def lista_planos_descontos(request):
    planos_descontos = Planos_Desconto.objects.all()
    return render(request, 'planos_desconto/lista_planos_descontos.html', {'planos_descontos': planos_descontos})