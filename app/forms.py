from django import forms
from app.models import *

class disciplina_form(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome']  # Inclua todos os campos que deseja que sejam editáveis no formulário
