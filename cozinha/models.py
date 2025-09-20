from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Prato(models.Model):
    nome = models.CharField(max_length=30)
    ingredientes = models.CharField(max_length=250)
    foto_cardapio = models.ImageField()
    foto_carrossel = models.ImageField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    adicionar_carrossel = models.BooleanField(default=False)


class Avaliacao(models.Model):
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    nome_cliente = models.CharField(max_length=30)
    resenha = models.TextField()
    foto_cliente = models.ImageField()


class Funcionario(models.Model):
    nome = models.CharField(max_length=40)
    cargo = models.CharField(max_length=30)
    foto = models.ImageField()
    bio = models.TextField()


class Contato(models.Model):
    TIPOS_SERVICOS = {
        "PC": "Personal Chef",
        "B": "Buffet",
        "JT": "Jantar Temático",
    }
    tipo_servico = models.CharField(max_length=2, choices=TIPOS_SERVICOS)
    nome_cliente = models.CharField(max_length=30)
    email = models.EmailField()
    descricao = models.TextField(blank=True)


class Reserva(models.Model):
    nome_cliente = models.CharField()
    telefone = models.CharField(max_length=11)
    data = models.DateField()
    horario = models.DateTimeField()
    qtd_pessoas = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    observacao = models.TextField()
