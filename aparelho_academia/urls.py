from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aparelhos_academia, name='lista_aparelhos_academia')
    ]