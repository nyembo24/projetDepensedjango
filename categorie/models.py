from django.db import models
from connexion.models import Connexion

class Categorie(models.Model):
    idcat = models.AutoField(primary_key=True)
    nomcat = models.CharField(max_length=100)

    matricule = models.ForeignKey(
        Connexion,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    def __str__(self):
        return self.nomcat
