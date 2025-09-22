from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def cardapio(request):
    return render(request, "cardapio.html")
