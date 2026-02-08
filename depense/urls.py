from django.contrib import admin
from django.urls import path
from . import views as viewDep
from connexion import views as viewsCon

urlpatterns = [
    path("home/",viewDep.ajouterDepense,name="ajouterDepense" ),
    path("", viewsCon.connexion, name="connexion"),
]
