from django.shortcuts import render
from .models import Aparelho_Academia

def lista_aparelhos_academia(request):
    aparelhos_academia = Aparelho_Academia.objects.all()
    return render(request, 'aparelho_academia/lista_aparelhos_academia.html', {'aparelhos_academia': aparelhos_academia})