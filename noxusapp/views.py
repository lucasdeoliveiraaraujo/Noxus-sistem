from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratorios
from .models import LaboratorioDisponibilidade
from .models import Menu

# Create your views here.

def menu(request):
    dadosenvio = json.loads(request.body)
    menus = Menu.objects.all()
    todosmenu = ""
    ativo = ""
    for menusitem in menus:
        menusitem.url = "/"+menusitem.url
        if not menusitem.url.find(dadosenvio["url"]):
            ativo = "active"
        else:
            ativo = ""

        todosmenu += f'''<li class="menu-item {ativo}">
                  <a href="http://127.0.0.1:8000{menusitem.url}" class="menu-link">
                      {menusitem.icone}
                      <div data-i18n="{menusitem.nome}">{menusitem.nome}</div>
                  </a>
              </li>'''
    return HttpResponse(todosmenu)


def novolaboratorio(request, id = None):
    if id != None:
        laboratorio = Laboratorios.objects.filter(id=id)
        return render(request, "noxusapp/novolaboratorio.html", context={"laboratorio": laboratorio.values()[0]})

    return render(request, 'noxusapp/novolaboratorio.html')
@csrf_exempt
def dellaboratorio(request):
    dadosenvio = json.loads(request.body)
    laboratorio = Laboratorios.objects.get(id=dadosenvio["id"])
    laboratorio.delete()
    return HttpResponse('{"tipo":"success","titulo":"Operção realizada com sucesso","mensagem":"Laboratorio apagado com sucesso!"}')

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

def login(request):
    return render(request,"noxusapp/login.html")

def esqueceusenha(request):
    return render(request,"noxusapp/esqueceusenha.html")

def novousuario(request):
    return render(request,"noxusapp/registrar.html")

def agendamentos(request):
    return render(request,"noxusapp/agendamentos.html")