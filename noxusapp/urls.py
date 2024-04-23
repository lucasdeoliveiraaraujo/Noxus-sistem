from django.urls import path

from . import views

urlpatterns = [
    path("", views.novolaboratorio, name="novolaboratorio"),
    path("", views.addLaboratorio, name="addLaboratorio")
]