from django.shortcuts import render
from .models import Avaliacao_Medica

def lista_avaliacoes_medicas(request):
    avaliacoes_medicas = Avaliacao_Medica.objects.all()
    return render(request, 'avaliacao_medica/lista_avaliacoes_medicas.html', {'avaliacoes_medicas': avaliacoes_medicas})