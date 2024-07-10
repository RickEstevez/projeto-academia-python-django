from django.shortcuts import render
from .models import Aula

def lista_aulas(request):
    aulas = Aula.objects.all()
    return render(request, 'aula/lista_aulas.html', {'aulas': aulas})