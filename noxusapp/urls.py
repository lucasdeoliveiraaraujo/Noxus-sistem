from django.urls import path, re_path

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
    path("alterarusuario/", views.alterarusuario, name="alterarusuario"),
    path("novousuario/", views.novousuario, name="novousuario"),
    path("agendamentos/", views.agendamentos, name="agendamentos"),
    path("obteragendamentos/", views.obteragendamentos, name="obteragendamentos"),
    path("obterdetalhamentoreserva/", views.obterdetalhamentoreserva, name="obterdetalhamentoreserva"),
    path("addcategoria/", views.addcategoria, name="addcategoria"),
    path("delcategoria/", views.delcategoria, name="delcategoria"),
    path("categorias/", views.categorias, name="categorias"),
    path("obterusuario/", views.buscausuario, name="obterusuario"),
    path("obterhorarios/<int:id>/", views.obterlaboratorio, name="obterhorarios"),
    path("usuarios/?P<int:id>/$", views.usuarios, name="meuusuario"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("addusuario/", views.addusuario, name="addusuario"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
    path("controleconfiguracao/<int:id>/", views.salvarconfiguracao, name="controleconfiguracao"),
    path("pesquisarlaboratorio/", views.pesquisarlaboratorio, name="pesquisarlaboratorio"),
    path("reservarlaboratorio/<int:id>/", views.reservarlaboratorio, name="reservarlaboratorio"),
    path("editaragendamento/<int:id>/", views.editaragendamento, name="editaragendamento"),
    path("obterhorariosreservados/", views.obterhorariosreservados, name="obterhorariosreservados"),
    path("addreserva/", views.addreserva, name="addreserva"),
    path("delreserva/", views.delreserva, name="delreserva")


]


