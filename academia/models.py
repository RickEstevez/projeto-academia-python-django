from django.db import models

class Academia(models.Model):

    Nome = models.CharField(max_length=100, null=False, blank=False)
    Legenda = models.CharField(max_length=150, null=False, blank=False)
    Descricao = models.TextField(null=False, blank=False)