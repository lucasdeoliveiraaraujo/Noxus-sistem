from django.db import models
# Create your models here.

class Laboratorios(models.Model):
    nomeLoboratorio = models.CharField(max_length=1000)
    local = models.CharField(max_length=4000)
    descricao = models.CharField(max_length=4000)
    id = models.IntegerField(primary_key=True)
    diaSemana = models.IntegerField()
    horaInicio = models.TimeField(max_length=4)
    horaTermino = models.TimeField(max_length=4)

    def __str__(self):
        return self.name