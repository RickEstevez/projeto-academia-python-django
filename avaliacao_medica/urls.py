from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_avaliacoes_medicas, name='lista_avaliacoes_medicas')
]