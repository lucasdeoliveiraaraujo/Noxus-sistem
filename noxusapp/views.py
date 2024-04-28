from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratorios
from .models import LaboratorioDisponibilidade
from .models import Menu

# Create your views here.

def menu(request):
    menus = Menu.objects.all()
    todosmenu = ""
    for menusitem in menus:
        todosmenu += f'''<li class="menu-item ">
                  <a href="http://127.0.0.1:8000/{menusitem.url}" class="menu-link">
                      {menusitem.icone}
                      <div data-i18n="{menusitem.nome}">{menusitem.nome}</div>
                  </a>
              </li>'''
    return HttpResponse(todosmenu)


def novolaboratorio(request, id=None):
    menus = menu(request)
    if id != None:
        laboratorio = Laboratorios.objects.get(id)
        return render(request, "noxusapp/novolaboratorio.html", context={"laboratorio": laboratorio, "menus": menus})

    return render(request, 'noxusapp/novolaboratorio.html', context={"menus": menus})


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
    return render(request, 'noxusapp/laboratorios.html', context={"laboratorios": laboratorios})



