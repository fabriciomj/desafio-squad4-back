from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContatoForm, ReservaForm
from .models import Prato


def index(request):
    destaques = Prato.objects.filter(tipo__exact="E")
    form_contato = ContatoForm()
    form_reserva = ReservaForm()
    if request.method == "POST":
        POST = request.POST
        if "form_contato" in POST:
            form_contato = ContatoForm(POST)
            if form_contato.is_valid():
                form_contato.save()
                return HttpResponseRedirect(reverse("index"))
        elif "form_reserva" in POST:
            form_reserva = ReservaForm(POST)
            if form_reserva.is_valid():
                form_reserva.save()
                return HttpResponseRedirect(reverse("index"))

    context = {
        "destaques": destaques,
        "form_contato": form_contato,
        "form_reserva": form_reserva,
    }
    return render(request, "index.html", context)


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
