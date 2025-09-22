from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cozinha"),
    path("cardapio/", views.cardapio, name="cardapio"),
]
