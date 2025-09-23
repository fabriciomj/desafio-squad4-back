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
    entradas = Prato.objects.filter(tipo__exact="E")
    principais = Prato.objects.filter(tipo__exact="PP")
    sobremesas = Prato.objects.filter(tipo__exact="S")
    pratos = {
        "entradas": entradas,
        "principais": principais,
        "sobremesas": sobremesas,
    }
    return render(request, "cardapio.html", pratos)


def sobre_nos(request):
    return render(request, "sobre-nos.html")
