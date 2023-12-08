from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=50, default='Sem Nome')
    PAPEL_CHOICES = (
        ('Aluno', 'Aluno'),
        ('Professor', 'Professor'),
    )
    papel = models.CharField(max_length=15, choices=PAPEL_CHOICES)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Usuario"  
        verbose_name_plural = "Usuarios" 


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Disciplina"  
        verbose_name_plural = "Disciplinas"  
        ordering = ['nome']


class Professor(models.Model):
    professor = models.OneToOneField(Usuario, on_delete=models.CASCADE, limit_choices_to={'papel': 'Professor'})
    disciplinas_ministradas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.professor.nome
    class Meta:
        verbose_name = "Professor"  
        verbose_name_plural = "Professores"  
        ordering = ['professor']

class Aluno(models.Model):
    aluno = models.OneToOneField(Usuario, on_delete=models.CASCADE, limit_choices_to={'papel': 'Aluno'})
    disciplinas_cursadas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.aluno.nome
    
    class Meta:
        verbose_name = "Aluno"  
        verbose_name_plural = "Alunos"  
        ordering = ['aluno']


class Horario(models.Model):
    DIA_DA_SEMANA_CHOICES = (
        ('Segunda', 'Segunda-feira'),
        ('Terca', 'Terça-feira'),
        ('Quarta', 'Quarta-feira'),
        ('Quinta', 'Quinta-feira'),
        ('Sexta', 'Sexta-feira'),
        ('Sabado', 'Sábado'),
    )

    HORA_DE_INICIO_CHOICES = (
        (1, '13:00'),
        (2, '13:55'),
        (3, '15:10'),
        (4, '16:05'),
        (5, '19:00'),
        (6, '19:55'),
        (7, '21:10'),
        (8, '22:05'),
    )

    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=20, choices=DIA_DA_SEMANA_CHOICES)
    hora_de_inicio = models.IntegerField(choices=HORA_DE_INICIO_CHOICES)

    def __str__(self):
        return f"{self.disciplina_associada} - {self.dia_da_semana}"

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"


# Create your models here.
