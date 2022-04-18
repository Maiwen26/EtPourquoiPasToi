from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.

class Temoignages(models.Model):
    temoignageId=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=150,blank=False)
    datePublication=models.DateField(auto_now_add=True,auto_now=False,blank=False)



class Utilisateurs(AbstractBaseUser):  #AbstractBaseUser continent que le champ password 
    utilisateurId=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,blank=False,unique=True)
    prenom=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=200,blank=False)
    
    #Création des choix pour le type d'utilisateur :
    LC='Lycéenne ou collégienne'
    I='Ingénieure ou étudiante ingénieure'
    A='Autre'

    TYPE_UTILISATEUR=((LC,'Lycéenne ou collégienne'),(I,'Ingénieure ou étudiante ingénieure'),(A,'Autre'))

    typeUtilisateur=models.CharField(max_length=50,choices=TYPE_UTILISATEUR,blank=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['nom','prenom','typeUtilisateur']
