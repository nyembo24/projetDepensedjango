from django.db import models
from categorie.models import Categorie

class Depense(models.Model):
    iddepense = models.AutoField(primary_key=True)
    nomdep = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    devise = models.CharField(max_length=3)
    date = models.DateField()
    idcat = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="depenses"
    )

    def __str__(self):
        return f"{self.nomdep} - {self.montant} - {self.devise}"
