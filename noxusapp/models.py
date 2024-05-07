from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nomeCategoria = models.CharField(max_length=50, blank=True, null=True)

class Laboratorios(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True)
    nomeLaboratorio = models.CharField(max_length=1000, null=True, blank=True)
    local = models.CharField(max_length=4000, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)

class LaboratorioDisponibilidade(models.Model):
    laboratorios = models.ForeignKey(Laboratorios, on_delete=models.CASCADE, blank=True, null=True)
    diaSemana = models.CharField(max_length=3, default=None, null=True, blank=True)
    horaInicio = models.TimeField(auto_now=False, null=True, blank=True)
    horaTermino = models.TimeField(auto_now=False, null=True, blank=True)

class LaboratorioAgendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    laboratorios = models.ForeignKey(Laboratorios, on_delete=models.CASCADE, blank=True, null=True)
    diaSemana = models.CharField(max_length=3, default=None, null=True, blank=True)
    horaInicio = models.TimeField(auto_now=False, null=True, blank=True)
    horaTermino = models.TimeField(auto_now=False, null=True, blank=True)


class Menu(models.Model):
    nome = models.CharField(max_length=50, default=None, null=True, blank=True)
    icone = models.CharField(max_length=1000, default=None, null=True, blank=True)
    url = models.CharField(max_length=200, default=None, null=True, blank=True)

class Configuracao(models.Model):
    emailnotificao = models.EmailField(max_length=200, default=None, null=True, blank=True)
    porta = models.IntegerField(default=None, null=True, blank=True)
    tls = models.BooleanField(default=True, null=True, blank=True)
    senha = models.CharField(max_length=500, default=None, null=True, blank=True)
    host = models.CharField(max_length=200, default=None, null=True, blank=True)
