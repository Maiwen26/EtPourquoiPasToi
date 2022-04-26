from email.policy import default
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
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
    def create_superuser(self,email,password=None,**extra_fields):
        gestionnaire=self.model(email=email)
        gestionnaire.set_password(password)
        gestionnaire.is_staff=True
        gestionnaire.is_admin=True
        gestionnaire.save(using=self._db)
        return gestionnaire

class Utilisateurs(AbstractBaseUser,PermissionsMixin):  #AbstractBaseUser continent que le champ password 
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
    

    #Nécessaire avec l'utilisation de AbstractBaseUser
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['nom','prenom','typeUtilisateur']

    #Pour la création d'un super utilisateur :
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    objects=UtilisateurGestionnaire()



#Quand un utilisateur s'inscrit un token est créé
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def creationAuthToken(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)






