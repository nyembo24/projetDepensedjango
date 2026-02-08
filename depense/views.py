from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Depense
from categorie.models import Categorie
from connexion.models import Connexion
def ajouterDepense(request):
    if not request.session.get("matricule"):
        return redirect("connexion")
    matriculeSession=request.session.get("matricule")
    utilisateur=Connexion.objects.get(matricule=matriculeSession)
    if request.method == "POST":
        nomdep=request.POST.get("nomdep")
        description=request.POST.get("description")
        montant=request.POST.get("montant")
        devise=request.POST.get("devise")
        date=request.POST.get("date")
        idcat=request.POST.get("idcat")
        idcategori=Categorie.objects.get(idcat=idcat,matricule=utilisateur)
        Depense.objects.create(
            nomdep=nomdep,
            description=description,
            montant=montant,
            devise=devise,
            date=date,
            idcat=idcategori
        )
        messages.success(request,"enregistrement effectuer avec succès")
    elif request.method == "GET" and request.GET.get("sup"):
        sup=request.GET.get("sup")
        Depense.objects.filter(iddepense=sup).delete()
        messages.success(request,"suppression effectuer avec succès")
    depense=Depense.objects.filter()
    categ = Categorie.objects.filter(matricule=utilisateur)
    return render(request, "home.html",{"categorie":categ,"depense":depense})