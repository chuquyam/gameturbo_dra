from django.forms import ModelForm, fields
from locadora.models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','CPF', 'email', 'telefone', 'idade' ]