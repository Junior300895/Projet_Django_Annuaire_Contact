from django.db import models

class Contact(models.Model):
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    numero = models.CharField(max_length=10,default="773012470")
    email = models.EmailField(max_length=20,default="abadaa9518@gmail.com")
    adresse = models.CharField(max_length=20)
    def __str__(self):
        return self.prenom
# class Repertoire(models.Model):
#





