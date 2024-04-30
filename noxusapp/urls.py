from django.urls import path

from . import views

urlpatterns = [
    path("novolaboratorio/", views.novolaboratorio, name="novolaboratorio"),
    path("editarlaboratorio/<int:id>/", views.novolaboratorio, name="editarlaboratorio"),
    path("addlaboratorio/", views.addlaboratorio, name="addlaboratorio"),
    path("laboratorios/", views.homelaboratorio, name="laboratorios"),
    path("dellaboratorio/", views.dellaboratorio, name="dellaboratorio"),
    path("menus/", views.menu, name="menu"),
    path("login/", views.login, name="login"),
    path("esqueceusenha/", views.esqueceusenha, name="esqueceusenha"),
    path("novousuario/", views.novousuario, name="esqueceusenha"),
    path("agendamentos/",views.agendamentos, name="agendamentos")
]

