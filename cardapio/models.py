from django.db import models

class Prato(models.Model):
    nome = models.CharField(max_length=30)
    ingredientes = models.CharField(max_length=250)
    foto_cardapio = models.ImageField()
    foto_carrossel = models.ImageField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)