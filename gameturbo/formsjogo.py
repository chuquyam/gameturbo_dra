from django.forms import ModelForm, fields
from locadora.models import Jogo

class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['titulo','tipo','fabricante','plataforma','faixaetaria','quantidade','preco' ]