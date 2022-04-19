from distutils.command.upload import upload
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Create your models here.

class Temoignages(models.Model):
    temoignageId=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=150,blank=False)
    datePublication=models.DateField(auto_now_add=True,auto_now=False,blank=False)
    domaineEtude=models.CharField(max_length=100,blank=False)

    #Création des choix pour le type de témoignage :
    T='Texte'
    A='Audio'
    V='Vidéo'

    TYPE_TEMOIGNAGE=((T,'Texte'),(A,'Audio'),(V,'Vidéo'))
    typeTemoignage=models.CharField(max_length=50,choices=TYPE_TEMOIGNAGE,blank=False)

    #Création des choix pour les différentes régions de France :
    ARA='Auvergne-Rhône-Alpes'
    BFC='Bourgogne-Franche-Comté'
    BRE='Bretagne'
    CVL='Centre-Val de Loire'
    COR='Corse'
    GES='Grand Est'
    HDF='Hauts-de-France'
    IDF='Île-de-France'
    NOR='Normandie'
    NAQ='Nouvelle-Aquitaine'
    OCC='Occitanie'
    PLD='Pays de la Loire'
    PAC='Provence-Alpes-Côte d\'Azur'
    GUA='Guadeloupe'
    GUF='Guyane'
    MTQ='Martinique'
    LRE='La Réunion'
    MAY='Mayotte'

    REGION=((ARA,'Auvergne-Rhône-Alpes'),(BFC,'Bourgogne-Franche-Comté'),(BRE,'Bretagne'),
    (CVL,'Centre-Val de Loire'),(COR,'Corse'),(GES,'Grand Est'),
    (HDF,'Hauts-de-France'),(IDF,'Île-de-France'),(NOR,'Normandie'),
    (NAQ,'Nouvelle-Aquitaine'),(OCC,'Occitanie'),(PLD,'Pays de la Loire'),
    (PAC,'Provence-Alpes-Côte d\'Azur'),(GUA,'Guadeloupe'),(GUF,'Guyane'),
    (MTQ,'Martinique'),(LRE,'La Réunion'),(MAY,'Mayotte'))
    region=models.CharField(max_length=50,choices=REGION,blank=False)

    #Création des différents types de contenu :
    contenu=models.FileField(upload_to='medias/',null=False,blank=False)

    #Création de la clée étrangère utilisateur liée au témoignage :
    creatrice=models.ForeignKey('Utilisateurs',on_delete=models.SET_NULL,null=True)




class Utilisateurs(AbstractBaseUser):  #AbstractBaseUser continent que le champ password 
    utilisateurId=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,blank=False,unique=True)
    prenom=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=200,blank=False)
    
    #Création des choix pour le type d'utilisateur :
    LC='Lycéenne ou collégienne'
    I='Ingénieure ou étudiante ingénieure'
    AU='Autre utilisateur.e'

    TYPE_UTILISATEUR=((LC,'Lycéenne ou collégienne'),(I,'Ingénieure ou étudiante ingénieure'),(AU,'Autre utilisateur.e'))
    typeUtilisateur=models.CharField(max_length=50,choices=TYPE_UTILISATEUR,blank=False)

    #Nécessaire avec l'utilisation de AbstractBaseUser
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['nom','prenom','typeUtilisateur']
