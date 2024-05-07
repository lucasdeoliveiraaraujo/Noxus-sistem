import django.contrib.auth.models
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Laboratorios, Configuracao, LaboratorioDisponibilidade, Menu, Categorias
from .classes.utils import nvl, gerarUsuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.


def handle404error(request, exception=None):
    return render(request, "not_found.html")


@login_required
def menu(request):
    dadosenvio = json.loads(request.body)
    menus = Menu.objects.all()
    todosmenu = ""
    ativo = ""
    for menusitem in menus:
        menusitem.url = "/" + menusitem.url
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


@login_required
def novolaboratorio(request, id: int = None):
    if id != None:
        laboratorio = Laboratorios.objects.filter(id=id)
        return render(request, "noxusapp/controlelaboratorio.html",
                      context={"laboratorio": laboratorio.values()[0], "rota": "noxus/atualizarlaboratorio/"})

    return render(request, 'noxusapp/controlelaboratorio.html', context={"rota": "noxus/addlaboratorio/"})


@csrf_exempt
@login_required
def dellaboratorio(request):
    dadosenvio = json.loads(request.body)
    laboratorio = Laboratorios.objects.get(id=dadosenvio["id"])
    laboratorio.delete()
    return HttpResponse(
        '{"tipo":"success","titulo":"Operção realizada com sucesso","mensagem":"Laboratorio apagado com sucesso!"}')


@login_required
@csrf_exempt
def obterlaboratorio(request, id: int = None):
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


@login_required
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
        disponibilidadelaboratorio = Laboratorios.objects.get(
            id=dadosenvio["id"]).laboratoriodisponibilidade_set.filter(diaSemana=str(diasemana).strip())
        for indicehorario, horario in enumerate(dadosenvio["horarios"][diasemana]):
            if indicehorario == 0:
                disponibilidadelaboratorio.update(horaInicio=horario)
            else:
                disponibilidadelaboratorio.update(horaTermino=horario)

    return HttpResponse('{"tipo":"success","titulo":"Dados salvos","mensagem":"Laboratorio salvo com sucesso"}')


@login_required
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


@login_required
def homelaboratorio(request):
    laboratorios = Laboratorios.objects.all()
    return render(request, 'noxusapp/laboratorios.html', context={"laboratorios": laboratorios})


def esqueceusenha(request):
    return render(request, "noxusapp/esqueceusenha.html")


def novousuario(request):
    return render(request, "noxusapp/registrar.html")


@login_required
def agendamentos(request):
    return render(request, "noxusapp/agendamentos.html")


@login_required
def addcategoria(request):
    dadosenvio = json.loads(request.body)
    categoria = Categorias()
    categoria.nomeCategoria = dadosenvio["nomeCategoria"]
    categoria.save()


@login_required
def categorias(request):
    categoria = Categorias.objects.values()
    arrayaux = []
    for item in categoria:
        arrayaux.append(item)

    jsonenvio = json.dumps({
        "categorias": arrayaux
    })

    return HttpResponse(jsonenvio)


@login_required
def usuarios(request, id=None):
    if id != None:
        usuario = User.objects.get(id=id)
        return render(request, "noxusapp/usuario.html", context={"usuario": usuario})
    return render(request, "noxusapp/usuario.html")


@login_required
def addusuario(request):
    dados = json.loads(request.body)
    nomeusuario = gerarUsuario(dados["nome"])
    try:
        User.objects.get(username=nomeusuario)
    except django.contrib.auth.models.User.DoesNotExist:
        usuario = User.objects.create_user(nomeusuario, dados["email"], dados["senha"])
        nome = dados["nome"].upper().split()
        sobrenome = ""
        for indice, nomes in enumerate(nome):
            if indice == 0:
                usuario.first_name = nomes
            else:
                sobrenome += f"{nomes} "

        usuario.last_name = sobrenome.strip()
        usuario.save()
        return HttpResponse('{"tipo": "success", "titulo": "Usuário criado", "mensagem": "Usuário criado com sucesso"}')


@login_required
def configuracoes(request):
    configuracoes = Configuracao.objects.filter(emailnotificao__isnull=False)
    return render(request, "noxusapp/configuracoes.html", context={"configuracoes": configuracoes.values()[0]})


@login_required
@csrf_exempt
def salvarconfiguracao(request, id: int = None):
    dados = json.loads(request.body)
    if len(Configuracao.objects.all()) == 0:
        configuracao = Configuracao()
        configuracao.emailnotificao = str(dados["emailRecuperacao"]).lower()
        if dados["tls"] == "S":
            configuracao.tls = True
        else:
            configuracao.tls = False

        configuracao.porta = int(dados["porta"])
        configuracao.senha = dados["senha"]
        configuracao.host = str(dados["hostname"]).strip()
        configuracao.save()
    else:
        configuracao = Configuracao.objects.get(id=id)
        configuracao.emailnotificao = str(dados["emailRecuperacao"]).lower()
        if dados["tls"] == "S":
            configuracao.tls = True
        else:
            configuracao.tls = False
        configuracao.porta = int(dados["porta"])
        configuracao.senha = dados["senha"]
        configuracao.host = str(dados["hostname"]).strip()
        configuracao.save()

    import sys
    sys.path.append("..")
    from Noxus.configuracao import alterarquivoconfig
    alterarquivoconfig("settings.ini")

    return HttpResponse('{"tipo":"success", "titulo": "Dados salvos com sucesso", "mensagem": "Configurações salvas"}')


@csrf_exempt
def pesquisarlaboratorio(request):
    dados = json.loads(request.body)
    print(dados)
    if dados["filtro"] == "nome":
        laboratorios = Laboratorios.objects.filter(nomeLaboratorio__contains=dados["pesquisa"])
    elif dados["filtro"] == "descricao":
        laboratorios = Laboratorios.objects.filter(descricao__contains=dados["pesquisa"])
    else:
        laboratorios = Laboratorios.objects.filter()

    jsonenvio = {
        "laboratorios": []
    }
    if laboratorios.count() > 0:
        # print(laboratorios.count())
        for laboratorio in laboratorios:
            jsonenvio["laboratorios"].append({
                "nomeLaboratorio": laboratorio.nomeLaboratorio,
                "descricao": laboratorio.descricao,
                "nomeCategoria": laboratorio.categoria.nomeCategoria,
                "id": laboratorio.id
            })
    return HttpResponse(json.dumps(jsonenvio))
