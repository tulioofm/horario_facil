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
            return redirect('disciplina-list')  

    else:
        form = disciplina_form()

    return render(request, 'disciplina_form.html', {'form': form})

def disciplina_update(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)

    if request.method == 'POST':
        form = disciplina_form(request.POST, instance=disciplina)  

        if form.is_valid():
            form.save() 
            return redirect('disciplina-list') 

    else:
        form = disciplina_form(instance=disciplina)  

    return render(request, 'disciplina_form.html', {'form': form, 'disciplina': disciplina})

def disciplina_delete(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    disciplina.delete()
    return redirect('disciplina-list')

def usuario_list(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuario_list.html',  usuarios)

def usuario_create(request):
    if request.method == 'POST':
        form = usuario_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('usuario-list') 

    else:
        form = usuario_form()

    return render(request, 'usuario_form.html', {'form': form})

def usuario_update(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)

    if request.method == 'POST':
        form = usuario_form(request.POST, instance=usuario)  

        if form.is_valid():
            form.save()  
            return redirect('usuario-list')  

    else:
        form = usuario_form(instance=usuario)  

    return render(request, 'usuario_form.html', {'form': form, 'usuario': usuario})

def usuario_delete(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    usuario.delete()
    return redirect('usuario-list')

def professor_list(request):
    professores = {
        'professores': Professor.objects.all()
    }
    return render(request, 'professor_list.html',  professores)

def professor_create(request):
    if request.method == 'POST':
        form = professor_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('professor-list')  

    else:
        form = professor_form()

    return render(request, 'professor_form.html', {'form': form})

def professor_update(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)

    if request.method == 'POST':
        form = professor_form(request.POST, instance=professor)  

        if form.is_valid():
            form.save()  
            return redirect('professor-list')  

    else:
        form = professor_form(instance=professor)  

    return render(request, 'professor_form.html', {'form': form, 'professor': professor})

def professor_delete(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    professor.delete()
    return redirect('professor-list')

def aluno_list(request):
    alunos = {
        'alunos': Aluno.objects.all()
    }
    return render(request, 'aluno_list.html',  alunos)

def aluno_create(request):
    if request.method == 'POST':
        form = aluno_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('aluno-list')  

    else:
        form = aluno_form()

    return render(request, 'aluno_form.html', {'form': form})

def aluno_update(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)

    if request.method == 'POST':
        form = aluno_form(request.POST, instance=aluno)  

        if form.is_valid():
            form.save()  
            return redirect('aluno-list')  

    else:
        form = aluno_form(instance=aluno)  

    return render(request, 'aluno_form.html', {'form': form, 'aluno': aluno})

def aluno_delete(request, aluno_id):
    aluno = get_object_or_404(aluno, pk=aluno_id)
    aluno.delete()
    return redirect('aluno-list')

def horario_list(request):
    horarios = {
        'horarios': Horario.objects.all()
    }
    return render(request, 'horario_list.html',  horarios)

def horario_create(request):
    if request.method == 'POST':
        form = horario_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('horario-list')  

    else:
        form = horario_form()

    return render(request, 'horario_form.html', {'form': form})

def horario_update(request, horario_id):
    horario = get_object_or_404(Horario, pk=horario_id)

    if request.method == 'POST':
        form = horario_form(request.POST, instance=horario)  

        if form.is_valid():
            form.save()  
            return redirect('horario-list')  

    else:
        form = horario_form(instance=horario)  

    return render(request, 'horario_form.html', {'form': form, 'horario': horario})

def horario_delete(request, horario_id):
    horario = get_object_or_404(horario, pk=horario_id)
    horario.delete()
    return redirect('horario-list')

# Create your views here.
