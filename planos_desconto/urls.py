from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_planos_descontos, name='lista_planos_descontos')
    ]