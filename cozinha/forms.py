from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    Textarea,
    NumberInput,
    DateTimeInput,
    TelInput,
)


from .models import Contato, Reserva


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ["tipo_servico", "nome_cliente", "email", "descricao"]
        widgets = {
            "nome_cliente": TextInput(attrs={"placeholder": "Seu nome"}),
            "email": EmailInput(attrs={"placeholder": "Email"}),
            "descricao": Textarea(attrs={"placeholder": "Descrição (opcional)"}),
        }


class MyDateTime(DateTimeInput):
    input_type = "datetime-local"


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ["nome_cliente", "telefone", "data_hora", "qtd_pessoas", "observacao"]
        widgets = {
            "nome_cliente": TextInput(attrs={"placeholder": "Nome completo"}),
            "telefone": TelInput(attrs={"placeholder": "Telefone"}),
            "data_hora": MyDateTime(),
            "qtd_pessoas": NumberInput(attrs={"placeholder": "Número de Assentos"}),
            "observacao": Textarea(attrs={"placeholder": "Observações (opcional)"}),
        }
