from email.policy import default
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

#Pour l'authification 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Création des modèles.

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
    utilisateurId=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True)


#Création du gestionnaire du site :

class UtilisateurGestionnaire(BaseUserManager):
    def create_superuser(self,email,password,is_staff=True,is_admin=True,*args,**kwargs):
        gestionnaire=self.model(
            email,
            password,
            is_staff,
            is_admin,
            *args,
            **kwargs,
            )
        gestionnaire.save(using=self._db)
        return gestionnaire



class Utilisateurs(AbstractBaseUser):  #AbstractBaseUser continent que le champ password 
    utilisateurId=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100,blank=False)
    prenom=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=200,blank=False,unique=True)
    
    #Création des choix pour le type d'utilisateur :
    LC='Lycéenne ou collégienne'
    I='Ingénieure ou étudiante ingénieure'
    AU='Autre utilisateur.e'

    TYPE_UTILISATEUR=((LC,'Lycéenne ou collégienne'),(I,'Ingénieure ou étudiante ingénieure'),(AU,'Autre utilisateur.e'))
    typeUtilisateur=models.CharField(max_length=50,choices=TYPE_UTILISATEUR,blank=False)
    """
    #nécessaire pour la création d'un admin :
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    last_login=models.DateTimeField(auto_now_add=True,null=True)
    """

    #Nécessaire avec l'utilisation de AbstractBaseUser
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['nom','prenom','typeUtilisateur']

    objects=UtilisateurGestionnaire()



#Quand un utilisateur s'inscrit un token est créé
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def creationAuthToken(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)






