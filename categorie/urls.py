from django.contrib import admin
from django.urls import path
from . import views as categorie_views
from connexion import views as connexion_views

urlpatterns = [
    path("categorie/", categorie_views.ajouterCategorie, name="ajouterCategorie"),
    path("", connexion_views.connexion, name="connexion"),
]
