"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('disciplinas/', disciplina_list, name='disciplina-list'),
    path('disciplinas/cadastrar/', disciplina_create, name='disciplina-create'),
    path('disciplinas/editar/<int:disciplina_id>/', disciplina_update, name='disciplina-update'),
    path('disciplinas/deletar/<int:disciplina_id>/', disciplina_delete, name='disciplina-delete'),
    path('usuarios/', usuario_list, name='usuario-list'),
    path('usuarios/cadastrar/', usuario_create, name='usuario-create'),
    path('usuarios/editar/<int:usuario_id>/', usuario_update, name='usuario-update'),
    path('usuarios/deletar/<int:usuario_id>/', usuario_delete, name='usuario-delete'),
    path('professores/', professor_list, name='professor-list'),
    path('professores/cadastrar/', professor_create, name='professor-create'),
    path('professores/editar/<int:professor_id>/', professor_update, name='professor-update'),
    path('professores/deletar/<int:professor_id>/', professor_delete, name='professor-delete'),
    path('alunos/', aluno_list, name='aluno-list'),
    path('alunos/cadastrar/', aluno_create, name='aluno-create'),
    path('alunos/editar/<int:aluno_id>/', aluno_update, name='aluno-update'),
    path('alunos/deletar/<int:aluno_id>/', aluno_delete, name='aluno-delete'),
    path('horarios/', horario_list, name='horario-list'),
    path('horarios/cadastrar/', horario_create, name='horario-create'),
    path('horarios/editar/<int:horario_id>/', horario_update, name='horario-update'),
    path('horarios/deletar/<int:horario_id>/', horario_delete, name='horario-delete'),
]
