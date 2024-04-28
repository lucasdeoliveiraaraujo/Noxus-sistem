from django.db import models

# Create your models here.
class Categorias(models.Model):
    nomeCategoria = models.CharField(max_length=50, blank=True, null=True)

class Laboratorios(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    nomeLaboratorio = models.CharField(max_length=1000, null=True, blank=True)
    local = models.CharField(max_length=4000, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)


class LaboratorioDisponibilidade(models.Model):
    laboratorios = models.ManyToManyField(Laboratorios)
    diaSemana = models.CharField(max_length=3, default=None, null=True, blank=True)
    horaInicio = models.TimeField(auto_now=False, null=True, blank=True)
    horaTermino = models.TimeField(auto_now=False, null=True, blank=True)
