from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContatoForm
from .models import Prato


def index(request):
    destaques = Prato.objects.filter(tipo__exact="E")
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ContatoForm()
    return render(request, "index.html", {"form": form, "destaques": destaques})


def cardapio(request):
    # Declara a tupla de tipos, em vez de usar TIPOS_PRATOS.keys() para garantir a ordem.
    tipos = ("E", "M", "V", "S", "B")
    categorias = [Prato.TIPOS_PRATOS[tipo] for tipo in tipos]

    # Pratos é uma lista de listas, na qual as sublistas são os pratos de um determinado tipo.
    pratos = []
    for tipo in tipos:
        pratos_cat_atual = []
        for prato in Prato.objects.filter(tipo__exact=tipo):
            pratos_cat_atual.append(prato)
        pratos.append(pratos_cat_atual)

    # Usa a função zip para ter fácil acesso aos nomes das categorias no template.
    cats_pratos = zip(categorias, pratos, strict=True)
    return render(request, "cardapio.html", {"cats_pratos": cats_pratos})


def sobre_nos(request):
    return render(request, "sobre-nos.html")
