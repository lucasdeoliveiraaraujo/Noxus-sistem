from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratorios
from .models import LaboratorioDisponibilidade
from .models import Menu
from .models import Categorias
from .classes.utils import nvl

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


def novolaboratorio(request, id:int=None):
    if id != None:
        laboratorio = Laboratorios.objects.filter(id=id)
        return render(request, "noxusapp/controlelaboratorio.html", context={"laboratorio":laboratorio.values()[0],"rota": "noxus/atualizarlaboratorio/"})

    return render(request, 'noxusapp/controlelaboratorio.html', context={"rota": "noxus/addlaboratorio/"})
@csrf_exempt
def dellaboratorio(request):
    dadosenvio = json.loads(request.body)
    laboratorio = Laboratorios.objects.get(id=dadosenvio["id"])
    laboratorio.delete()
    return HttpResponse('{"tipo":"success","titulo":"Operção realizada com sucesso","mensagem":"Laboratorio apagado com sucesso!"}')

@csrf_exempt
def obterlaboratorio(request, id:int=None):
    horarios = Laboratorios.objects.get(id=id).laboratoriodisponibilidade_set.all()
    dadosenvio = {
        "horarios": {
            "Dom": [],
            "Seg": [],
            "Ter": [],
            "Qua": [],
            "Qui": [],
            "Sex": [],
            "Sab": []
        }
    }
    for horario in horarios.values():
        dadosenvio["horarios"][f"{horario['diaSemana']}"].append(nvl(str(horario["horaInicio"]), ""))
        dadosenvio["horarios"][f"{horario['diaSemana']}"].append(nvl(str(horario["horaTermino"]), ""))


    print(dadosenvio)
    return HttpResponse(json.dumps(dadosenvio))
@csrf_exempt
def atualizarlaboratorio(request):
    dadosenvio = json.loads(request.body)
    laboratorio = Laboratorios.objects.get(id=dadosenvio["id"])
    categoria = Categorias.objects.get(id=dadosenvio["categoriaLaboratorio"])
    laboratorio.descricao = str(dadosenvio["descricaoLaboratorio"]).strip()
    laboratorio.nomeLaboratorio = str(dadosenvio["nomeLaboratorio"]).strip()
    laboratorio.local = str(dadosenvio["localizacao"]).strip()
    laboratorio.categoria_id = categoria.id
    laboratorio.save()

    for diasemana in dadosenvio["horarios"]:
        disponibilidadelaboratorio = Laboratorios.objects.get(id=dadosenvio["id"]).laboratoriodisponibilidade_set.filter(diaSemana=str(diasemana).strip())
        for indicehorario, horario in enumerate(dadosenvio["horarios"][diasemana]):
            if indicehorario == 0:
                disponibilidadelaboratorio.update(horaInicio=horario)
            else:
                disponibilidadelaboratorio.update(horaTermino=horario)

    return HttpResponse('{"tipo":"success","titulo":"Dados salvos","mensagem":"Laboratorio salvo com sucesso"}')

@csrf_exempt
def addlaboratorio(request):
    dadosenvio = json.loads(request.body)
    laboratorio = Laboratorios()
    disponibilidadelaboratorio = LaboratorioDisponibilidade()
    categoria = Categorias.objects.get(id=dadosenvio["categoriaLaboratorio"])
    laboratorio.descricao = str(dadosenvio["descricaoLaboratorio"]).strip()
    laboratorio.nomeLaboratorio = str(dadosenvio["nomeLaboratorio"]).strip()
    laboratorio.local = str(dadosenvio["localizacao"]).strip()
    laboratorio.categoria_id = categoria.id
    laboratorio.save()

    for diasemana in dadosenvio["horarios"]:
        disponibilidadelaboratorio.diaSemana = str(diasemana).strip()
        for indicehorario, horario in enumerate(dadosenvio["horarios"][diasemana]):
            if indicehorario == 0:
                disponibilidadelaboratorio.horaInicio = horario
            else:
                disponibilidadelaboratorio.horaTermino = horario

        disponibilidadelaboratorio.laboratorios_id = laboratorio.id

    return HttpResponse('{"tipo":"success","titulo":"Dados salvos","mensagem":"Laboratorio salvo com sucesso"}')


def homelaboratorio(request):
    laboratorios = Laboratorios.objects.all()
    return render(request, 'noxusapp/laboratorios.html', context={"laboratorios": laboratorios})

def login(request):
    return render(request, "noxusapp/login.html")

def esqueceusenha(request):
    return render(request, "noxusapp/esqueceusenha.html")

def novousuario(request):
    return render(request, "noxusapp/registrar.html")

def agendamentos(request):
    return render(request, "noxusapp/agendamentos.html")

def addcategoria(request):
    dadosenvio = json.loads(request.body)
    categoria = Categorias()
    categoria.nomeCategoria = dadosenvio["nomeCategoria"]
    categoria.save()

def categorias(request):
    categoria = Categorias.objects.values()
    arrayaux = []
    for item in categoria:
        arrayaux.append(item)

    jsonenvio = json.dumps({
        "categorias": arrayaux
    })


    return HttpResponse(jsonenvio)
