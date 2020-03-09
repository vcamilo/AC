from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):

    data_nascimento = forms.DateField()

    class Meta():
        model = Contato
        fields = ['nome', 'telefone', 'email', 'data_nascimento']