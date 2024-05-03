from django.urls import path

from . import views

urlpatterns = [
    path("controlelaboratorio/", views.novolaboratorio, name="controlelaboratorio"),
    path("controlelaboratorio/<int:id>/", views.novolaboratorio, name="controlelaboratorio"),
    path("addlaboratorio/", views.addlaboratorio, name="addlaboratorio"),
    path("laboratorios/", views.homelaboratorio, name="laboratorios"),
    path("dellaboratorio/", views.dellaboratorio, name="dellaboratorio"),
    path("menus/", views.menu, name="menu"),
    path("login/", views.login, name="login"),
    path("esqueceusenha/", views.esqueceusenha, name="esqueceusenha"),
    path("novousuario/", views.novousuario, name="esqueceusenha"),
    path("agendamentos/", views.agendamentos, name="agendamentos"),
    path("addcategoria/", views.addcategoria, name="addcategoria"),
    path("categorias/", views.categorias, name="categorias"),
    path("obterhorarios/<int:id>/", views.obterlaboratorio, name="obterhorarios")
]

