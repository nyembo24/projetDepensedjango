from django.urls import path
from . import views
from depense import views as depense_views

urlpatterns = [
    path("", views.connexion, name="connexion"),
    path("inscription/", views.inscription, name="inscription"),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("home/", depense_views.ajouterDepense, name="ajouterDepense"),
]
