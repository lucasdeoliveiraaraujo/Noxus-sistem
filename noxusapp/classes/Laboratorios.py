from django.db import models

class Laboratorio(models.Model):
    nomeLaboratorio = models.CharField(max_length=1000)
    local = models.CharField(max_lenght=4000)
    descricao = models.CharField(max_length=4000)
    diaSemana = models.IntegerField(max_lenght=1)
    horaInicio = models.TimeField(max_length=4)
    horaTermino = models.TimeField(max_length=4)
