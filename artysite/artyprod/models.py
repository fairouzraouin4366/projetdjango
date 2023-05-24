from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Rest of your code

# Create your models here.
class Service(models.Model):
    TYPE_CHOICES=[  ('dg','design graphique'),
                    ('pa','production audiovisuelle'),
                    ('3D','Conception 3D')]
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='')
    description=models.TextField(default='non définie')
    servPhoto= models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.type+","+self.description
class Personnel(models.Model):
    nom = models.CharField(max_length=100, null=True)
    prenom = models.CharField(max_length=100, null=True)
    date_naissance = models.DateField(null=True)
    cvPrs= models.FileField(upload_to='media/', blank=True, null=True)
    photoPrs = models.FileField(upload_to='media/', blank=True, null=True)
    linkedln = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} "

class Equipe(models.Model):
    nom = models.CharField(max_length=255)
    personnels = models.ManyToManyField(Personnel, related_name='equipes')

    def __str__(self):
        return self.nom 

class Projet(models.Model):
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE,null=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True)
    TYPE_CHOICES=[('o','acheve'),
                    ('n','en cours')]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='non définie')
    date_debut=models.DateField()
    date_fin=models.DateField()
    achevée = models.CharField(max_length=2,choices=TYPE_CHOICES)
    prjphtonr = models.ImageField(upload_to='media/', null=True, blank=True)

def __str__(self):
        return self.libellé+","+self.description+","+self.date_debut+","+self.date_fin+","+self.achevée
class ProjetRealise(models.Model):
    nom = models.CharField(max_length=255,default="")
    description:models.CharField(max_length=255,default="")
    services = models.ForeignKey('Service', on_delete=models.CASCADE, null=True)
    TYPE_CHOICES=[  ('Charte graphique ','Charte graphique '),
                    ('Objet  3D ','Objet  3D '),
                    ('Scénarisation','Scénarisation')]
    photoPrj = models.FileField(upload_to='media/', blank=True, null=True)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE,null=True)
    date_realisation= models.DateField(null=True, default=date.today)

    def __str__(self):
        return self.nom
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class DemandeProjet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    date_depot = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom
    
class Blog(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    datedep= models.DateField(null=True, default=date.today)
    source=models.URLField(blank=True, null=True)
    imgblog=models.ImageField(upload_to='media/', null=True, blank=True)

