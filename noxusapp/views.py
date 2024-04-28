from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratorios
from .models import LaboratorioDisponibilidade


# Create your views here.


def novolaboratorio(request):
    return render(request, 'noxusapp/novolaboratorio.html')


@csrf_exempt
def addlaboratorio(request):
    dadosenvio = json.loads(request.body)
    laboratorio = Laboratorios()
    laboratorio.descricao = str(dadosenvio["descricaoLaboratorio"]).strip()
    laboratorio.nomeLaboratorio = str(dadosenvio["nomeLaboratorio"]).strip()
    laboratorio.local = str(dadosenvio["localizacao"]).strip()
    laboratorio.descricao = str(dadosenvio["categoriaLaboratorio"]).strip()
    laboratorio.save()
    disponibilidadelaboratorio = LaboratorioDisponibilidade()

    for diaSemana in dadosenvio["horarios"]:
        disponibilidadelaboratorio = LaboratorioDisponibilidade()
        disponibilidadelaboratorio.diaSemana = str(diaSemana).strip()
        hora = 1
        for horario in dadosenvio["horarios"][diaSemana]:
            print(horario)
            print(hora)
            if hora == 1:
                disponibilidadelaboratorio.horaInicio = horario
            else:
                disponibilidadelaboratorio.horaTermino = horario
            hora += 1

        disponibilidadelaboratorio.save()
        disponibilidadelaboratorio.laboratorios.add(laboratorio.id)

    return HttpResponse('{"tipo":"success","titulo":"Dados salvos","mensagem":"Laboratorio salvo com sucesso"}')


def homelaboratorio(request):
    laboratorios = Laboratorios.objects.all()
    print(laboratorios.values())
    return render(request, 'noxusapp/laboratorios.html')
