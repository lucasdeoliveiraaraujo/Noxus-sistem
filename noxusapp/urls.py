from django.urls import path

from . import views

urlpatterns = [
    path("novolaboratorio/", views.novolaboratorio, name="novolaboratorio"),
    path("addlaboratorio/", views.addlaboratorio, name="addlaboratorio"),
    path("laboratorios/", views.homelaboratorio, name="laboratorios"),
    path("menus/", views.menu, name="menu")
]

