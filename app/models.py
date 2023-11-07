from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=50, default='Sem Nome')
    PAPEL_CHOICES = (
        ('Aluno', 'Aluno'),
        ('Professor', 'Professor'),
    )
    papel = models.CharField(max_length=15, choices=PAPEL_CHOICES)
    # Outros campos relacionados aos usuários, se necessário

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Usuario"  # Nome singular legível por humanos
        verbose_name_plural = "Usuarios"  # Nome plural legível por humanos


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    # Outros campos relacionados às disciplinas

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"  # Nome singular legível por humanos
        verbose_name_plural = "Disciplinas"  # Nome plural legível por humanos
        ordering = ['nome']


class Professor(models.Model):
    professor = models.OneToOneField(Usuario, on_delete=models.CASCADE, limit_choices_to={'papel': 'Professor'})
    disciplinas_ministradas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.professor.nome
    class Meta:
        verbose_name = "Professor"  # Nome singular legível por humanos
        verbose_name_plural = "Professores"  # Nome plural legível por humanos
        ordering = ['professor']

""""
class Turma(models.Model):
    nome = models.CharField(max_length=50, default='Sem Nome')
    alunos_matriculados = models.ManyToManyField(Usuario, limit_choices_to={'papel': 'Aluno'})
    disciplinas_da_turma = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)
    class Meta:
        verbose_name = "Turma"  # Nome singular legível por humanos
        verbose_name_plural = "Turmas"  # Nome plural legível por humanos
"""

class Aluno(models.Model):
    aluno = models.OneToOneField(Usuario, on_delete=models.CASCADE, limit_choices_to={'papel': 'Aluno'})
    disciplinas_cursadas = models.ManyToManyField(Disciplina)
    # Outros campos relacionados aos alunos, se necessário

    def __str__(self):
        return self.aluno.nome
    
    class Meta:
        verbose_name = "Aluno"  # Nome singular legível por humanos
        verbose_name_plural = "Alunos"  # Nome plural legível por humanos
        ordering = ['aluno']


class Horario(models.Model):
    DIA_DA_SEMANA_CHOICES = (
        ('Segunda', 'Segunda-feira'),
        ('Terca', 'Terça-feira'),
        ('Quarta', 'Quarta-feira'),
        ('Quinta', 'Quinta-feira'),
        ('Sexta', 'Sexta-feira'),
        # Adicione outros dias da semana conforme necessário
    )

    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=20, choices=DIA_DA_SEMANA_CHOICES)
    hora_de_inicio = models.TimeField()
    hora_de_termino = models.TimeField()
    # Outros campos relacionados aos horários

    def __str__(self):
        return f"{self.disciplina_associada} - {self.dia_da_semana}"
    class Meta:
        verbose_name = "Horario"  # Nome singular legível por humanos
        verbose_name_plural = "Horarios"  # Nome plural legível por humanos


# Create your models here.
