from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from app.models import *
from app.forms import *

def disciplina_list(request):
    disciplinas = {
        'disciplinas': Disciplina.objects.all()
    }
    return render(request, 'disciplina_list.html',  disciplinas)

def disciplina_create(request):
    if request.method == 'POST':
        form = disciplina_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('disciplina-list')  # Redirecione para a página de listagem de disciplinas após a criação

    else:
        form = disciplina_form()

    return render(request, 'disciplina_form.html', {'form': form})

def disciplina_update(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)

    if request.method == 'POST':
        form = disciplina_form(request.POST, instance=disciplina)  # Preencha o formulário com os dados da disciplina existente

        if form.is_valid():
            form.save()  # Salve as alterações no banco de dados
            return redirect('disciplina-list')  # Redirecione para a página de listagem de disciplinas

    else:
        form = disciplina_form(instance=disciplina)  # Crie um formulário preenchido com os dados da disciplina existente

    return render(request, 'disciplina_form.html', {'form': form, 'disciplina': disciplina})

def disciplina_delete(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    disciplina.delete()
    return redirect('disciplina-list')

# Create your views here.
