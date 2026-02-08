from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Connexion(models.Model):
    matricule = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=255)
    nom = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Hasher le mot de passe seulement s'il n'est pas déjà hashé
        if not self.password or not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.matricule} - {self.nom}"
