from django import forms
from app.models import *

class disciplina_form(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome'] 

class usuario_form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'papel'] 

class professor_form(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['professor', 'disciplinas_ministradas'] 

class aluno_form(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class horario_form(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
