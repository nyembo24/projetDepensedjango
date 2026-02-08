from django.shortcuts import render,redirect
from .models import Categorie
from django.contrib import messages
from connexion.models import Connexion

def ajouterCategorie(request):
    if not request.session.get("matricule"):
        return redirect("connexion")
    else:
        matricule_session = request.session.get("matricule")
        utilisateur = Connexion.objects.get(matricule=matricule_session)
        if request.method == "POST":
            mod = request.GET.get("mod")
            nomcatmod = request.POST.get("nomcatmod")
            if mod and nomcatmod:
                Categorie.objects.filter(idcat=mod).update(nomcat=nomcatmod)
                messages.success(request, "Modification effectuer avec succès")
                return redirect("ajouterCategorie")

            nomcat = request.POST.get("nomcat")
            if nomcat:
                Categorie.objects.create(
                    nomcat=nomcat,
                    matricule=utilisateur
                )
                messages.success(request, "Enregistrement effectuer avec succès")
                return redirect("ajouterCategorie")
            messages.error(request, "Le nom de la catégorie est obligatoire")
        elif request.method == "GET" and request.GET.get("sup"):
            mod=request.GET.get("sup")
            Categorie.objects.filter(idcat=mod).delete()
            messages.success(request,"suppression effectuer avec succès")
        elif request.method=="GET" and request.GET.get("mod") and request.GET.get("mod") is not None:
            valeur=Categorie.objects.filter(idcat=request.GET.get("mod"))
            return render(request, "categorie.html", {"valeur": valeur})
        categories = Categorie.objects.filter(matricule=utilisateur)
        return render(request, "categorie.html",{"categories":categories})
