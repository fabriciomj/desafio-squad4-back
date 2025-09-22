import os

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def gerar_nome_arquivo(
    m: models.Model, img: models.ImageField, nome: models.CharField
) -> str:
    """Recebe um Model, um ImageField e um CharField, retorna um novo nome para
    o arquivo no formato 'caminho/id_nome_ultimonome.ext'."""
    nome_arquivo = img.name
    bn = os.path.basename(nome_arquivo)
    dir = nome_arquivo.removesuffix(bn)
    ext = os.path.splitext(nome_arquivo)[-1]

    novo_nome = nome.lower()
    nome_split = novo_nome.split()
    novo_nome = str(m.id) + "_" + nome_split[0]

    if len(nome_split) > 1:
        novo_nome += "_" + nome_split[-1]

    return dir + novo_nome + ext


def renomear_imagem(path: str, novo_nome: str):
    """Recebe o path de um ImageField e o possível novo nome para o arquivo,
    renomeando o arquivo se já existir na pasta media."""
    if os.path.exists(path):
        caminho_novo = path.join(settings.MEDIA_ROOT, novo_nome)
        os.rename(path, caminho_novo)


class Prato(models.Model):
    nome = models.CharField(max_length=30)
    ingredientes = models.CharField(max_length=250)
    foto_cardapio = models.ImageField(upload_to="pratos")
    foto_carrossel = models.ImageField(blank=True, upload_to="pratos/destaque")
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    adicionar_carrossel = models.BooleanField(
        verbose_name="Destacar Prato", default=False
    )

    def save(self, **kwargs):
        novo_nome = gerar_nome_arquivo(self, self.foto_cardapio, self.nome)
        renomear_imagem(self.foto_cardapio.path, novo_nome)
        self.foto_cardapio.name = novo_nome
        if self.foto_carrossel:
            novo_nome = gerar_nome_arquivo(self, self.foto_carrossel, self.nome)
            renomear_imagem(self.foto_carrossel.path, novo_nome)
            self.foto_carrossel.name = novo_nome
        super().save(**kwargs)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    nome_cliente = models.CharField(max_length=30, verbose_name="Nome do Cliente")
    resenha = models.TextField()
    foto_cliente = models.ImageField(
        verbose_name="Foto do Cliente", upload_to="avaliacoes"
    )

    def save(self, **kwargs):
        novo_nome = gerar_nome_arquivo(self, self.foto_cliente, self.nome_cliente)
        renomear_imagem(self.foto_cliente.path, novo_nome)
        self.foto_cliente.name = novo_nome
        super().save(**kwargs)

    def __str__(self):
        return self.nome_cliente


class Funcionario(models.Model):
    nome = models.CharField(max_length=40)
    cargo = models.CharField(max_length=30)
    foto = models.ImageField(upload_to="funcionarios")
    bio = models.TextField(verbose_name="Biografia")

    def save(self, **kwargs):
        novo_nome = gerar_nome_arquivo(self, self.foto, self.nome)
        renomear_imagem(self.foto.path, novo_nome)
        self.foto.name = novo_nome
        super().save(**kwargs)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"


class Contato(models.Model):
    TIPOS_SERVICOS = {
        "PC": "Personal Chef",
        "B": "Buffet",
        "JT": "Jantar Temático",
    }
    tipo_servico = models.CharField(
        max_length=2, choices=TIPOS_SERVICOS, verbose_name="Tipo do Serviço"
    )
    nome_cliente = models.CharField(max_length=30, verbose_name="Nome do Cliente")
    email = models.EmailField()
    descricao = models.TextField(blank=True, verbose_name="Descrição")

    def __str__(self):
        return f"{self.nome_cliente} ({self.email}) - {self.TIPOS_SERVICOS[self.tipo_servico]}"


class Reserva(models.Model):
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome do Cliente")
    telefone = models.CharField(max_length=11)
    data = models.DateField()
    horario = models.DateTimeField(verbose_name="Horário")
    qtd_pessoas = models.IntegerField(
        verbose_name="Quantidade de pessoas",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    observacao = models.TextField(verbose_name="Observação")

    def __str__(self):
        return f"{self.nome_cliente} ({self.telefone}) - {self.data} {self.horario}"
