from django import forms
from .models import Plano

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'velocidade', 'preco', 'descricao', 'ativo']