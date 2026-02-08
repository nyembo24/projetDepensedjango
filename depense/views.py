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
        mod = request.GET.get("mod")
        nomdepmod = request.POST.get("nomdepmod")
        if mod:
            if not nomdepmod:
                messages.error(request, "Le nom de la dépense est obligatoire")
                depense=Depense.objects.filter(idcat__matricule=utilisateur)
                categ = Categorie.objects.filter(matricule=utilisateur)
                valeur=Depense.objects.filter(
                    iddepense=mod,
                    idcat__matricule=utilisateur
                ).first()
                return render(request, "home.html", {"categorie":categ,"depense":depense,"valeur":valeur})

            descriptionmod = request.POST.get("descriptionmod")
            montantmod = request.POST.get("montantmod")
            devisemod = request.POST.get("devisemod")
            datemod = request.POST.get("datemod")
            idcatmod = request.POST.get("idcatmod")
            idcategori = Categorie.objects.get(idcat=idcatmod, matricule=utilisateur)
            Depense.objects.filter(
                iddepense=mod,
                idcat__matricule=utilisateur
            ).update(
                nomdep=nomdepmod,
                description=descriptionmod,
                montant=montantmod,
                devise=devisemod,
                date=datemod,
                idcat=idcategori
            )
            messages.success(request,"Modification effectuer avec succès")
            return redirect("ajouterDepense")

        nomdep=request.POST.get("nomdep")
        description=request.POST.get("description")
        montant=request.POST.get("montant")
        devise=request.POST.get("devise")
        date=request.POST.get("date")
        idcat=request.POST.get("idcat")
        if nomdep and montant and devise and date and idcat:
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
            return redirect("ajouterDepense")
        messages.error(request, "Tous les champs obligatoires doivent etre remplis")
    elif request.method == "GET" and request.GET.get("sup"):
        sup=request.GET.get("sup")
        Depense.objects.filter(iddepense=sup, idcat__matricule=utilisateur).delete()
        messages.success(request,"suppression effectuer avec succès")
    elif request.method=="GET" and request.GET.get("mod") and request.GET.get("mod") is not None:
        mod = request.GET.get("mod")
        valeur=Depense.objects.filter(
            iddepense=mod,
            idcat__matricule=utilisateur
        ).first()
        depense=Depense.objects.filter(idcat__matricule=utilisateur)
        categ = Categorie.objects.filter(matricule=utilisateur)
        return render(request, "home.html", {"valeur": valeur,"categorie":categ,"depense":depense})
    depense=Depense.objects.filter(idcat__matricule=utilisateur)
    categ = Categorie.objects.filter(matricule=utilisateur)
    return render(request, "home.html",{"categorie":categ,"depense":depense})
