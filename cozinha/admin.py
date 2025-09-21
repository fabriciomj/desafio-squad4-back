from django.contrib import admin

from .models import Avaliacao, Contato, Funcionario, Prato, Reserva

for model in (Avaliacao, Contato, Funcionario, Prato, Reserva):
    admin.site.register(model)
