from django.urls import path

from . import views

urlpatterns = [
    path("controlelaboratorio/", views.novolaboratorio, name="controlelaboratorio"),
    path("controlelaboratorio/<int:id>/", views.novolaboratorio, name="controlelaboratorio"),
    path("atualizarlaboratorio/", views.atualizarlaboratorio, name="atualizarlaboratorio"),
    path("addlaboratorio/", views.addlaboratorio, name="addlaboratorio"),
    path("laboratorios/", views.homelaboratorio, name="laboratorios"),
    path("dellaboratorio/", views.dellaboratorio, name="dellaboratorio"),
    path("menus/", views.menu, name="menu"),
    path("esqueceusenha/", views.esqueceusenha, name="esqueceusenha"),
    path("novousuario/", views.novousuario, name="novousuario"),
    path("agendamentos/", views.agendamentos, name="agendamentos"),
    path("addcategoria/", views.addcategoria, name="addcategoria"),
    path("categorias/", views.categorias, name="categorias"),
    path("obterhorarios/<int:id>/", views.obterlaboratorio, name="obterhorarios"),
    path("usuarios/<int:id>/", views.usuarios, name="usuarios"),
    path("usuarios/", views.usuarios, name="usuarios", kwargs={'id': None},),
    path("addusuario/", views.addusuario, name="addusuario"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
    path("controleconfiguracao/<int:id>/", views.salvarconfiguracao, name="controleconfiguracao"),
    path("pesquisarlaboratorio/", views.pesquisarlaboratorio, name="pesquisarlaboratorio"),
    path("reservarlaboratorio/<int:id>/", views.reservarlaboratorio, name="reservarlaboratorio"),
    path("obterhorariosreservados/", views.obterhorariosreservados, name="obterhorariosreservados"),
    path("addreserva/", views.addreserva, name="addreserva")
]


