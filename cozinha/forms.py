from django.forms import ModelForm, TextInput, EmailInput, Textarea


from .models import Contato


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ["tipo_servico", "nome_cliente", "email", "descricao"]
        widgets = {
            "nome_cliente": TextInput(attrs={"placeholder": "Seu nome"}),
            "email": EmailInput(attrs={"placeholder": "Email"}),
            "descricao": Textarea(attrs={"placeholder": "Descrição (opcional)"}),
        }
