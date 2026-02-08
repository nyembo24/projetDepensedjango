from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Connexion

def connexion(request):
    if request.method == "POST":
        matricule = request.POST.get("matricule")
        password = request.POST.get("password")
        #print('password')
        #breakpoint()
        try:
            user = Connexion.objects.get(matricule=matricule)
            

            if user.check_password(password):
                # Sauvegarder l'utilisateur dans la session
                request.session["matricule"] = user.matricule
                request.session["nom"] = user.nom

                return redirect("ajouterDepense")
            else:
                messages.error(request, "Matricule ou mots de passe incorrecte")
        except Connexion.DoesNotExist:
            messages.error(request, "Matricule ou mots de passe incorrecte")

    return render(request, "connexion/connexion.html")


def inscription(request):
    if request.method == "POST":
        matricule = request.POST.get("matricule")
        nom = request.POST.get("nom")
        password = request.POST.get("password")

        # Vérifier si le matricule existe déjà
        if Connexion.objects.filter(matricule=matricule).exists():
            messages.error(request, "Ce matricule existe déjà")
            return redirect("inscription")

        # Création de l'utilisateur (password sera hashé automatiquement)
        Connexion.objects.create(
            matricule=matricule,
            nom=nom,
            password=password
        )

        messages.success(request, "Inscription réussie, veuillez vous connecter")
        return redirect("connexion")

    return render(request, "connexion/inscription.html")


def deconnexion(request):
    # Détruire toute la session
    request.session.flush()
    messages.success(request, "Vous avez été déconnecté avec succès")
    return redirect("connexion")
