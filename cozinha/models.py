from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Prato(models.Model):
    nome = models.CharField(max_length=30)
    ingredientes = models.CharField(max_length=250)
    foto_cardapio = models.ImageField()
    foto_carrossel = models.ImageField(blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    adicionar_carrossel = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    nome_cliente = models.CharField(max_length=30)
    resenha = models.TextField()
    foto_cliente = models.ImageField()

    def __str__(self):
        return self.nome_cliente


class Funcionario(models.Model):
    nome = models.CharField(max_length=40)
    cargo = models.CharField(max_length=30)
    foto = models.ImageField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.nome} - {self.cargo}"


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

    def __str__(self):
        return f"{self.tipo_servico} - {self.nome} ({self.email})"


class Reserva(models.Model):
    nome_cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    data = models.DateField()
    horario = models.DateTimeField()
    qtd_pessoas = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    observacao = models.TextField()

    def __str__(self):
        return f"{self.nome_cliente} ({self.telefone}) - {self.data} {self.horario}"
