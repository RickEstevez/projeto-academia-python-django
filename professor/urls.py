from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_professores, name='lista_professores'),
    # Outras URLs do app Professor
]