from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContatoForm


def index(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ContatoForm()
    return render(request, "index.html", {"form": form})


def cardapio(request):
    return render(request, "cardapio.html")


def sobre_nos(request):
    return render(request, "sobre-nos.html")
