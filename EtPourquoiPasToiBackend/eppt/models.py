import email
from pyexpat import model
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Temoignage(models.Model):
    """A typical class defining a model, derived from the Model class."""

    titreTemoignage = models.CharField(
        max_length=150, help_text='Entrez le nom de votre témoignage', unique=True, blank=False)

    TYPE_TEMOIGNAGE = [('V', 'video'), ('A', 'audio'), ('T', 'texte')]
    typeTemoignage = models.CharField(
        max_length=1, choices=TYPE_TEMOIGNAGE, blank=False)

    datePublication = models.DateField(auto_now_add=True,auto_now=False,blank=True)

    contenu = models.FileField()

    REGION = [('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France',
                                                                                                                                                                                                      'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ('Provence-Alpes-Côte d\'Azur', 'Provence-Alpes-Côte d\'Azur')]
    region = models.CharField(max_length=50, choices=REGION, blank=False)

    domaineEtude = models.CharField(max_length=50, blank=False)

    # Metadata
    class Meta:
        ordering = ['datePublication', '-titreTemoignage']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.titreTemoignage

class Utilisateur(models.Model):
    prenom=models.CharField(max_length=50, help_text='Entrez le nom de votre prénom', blank=False)

    nom=models.CharField(max_length=50, help_text='Entrez le nom de votre nom', blank=False)

    email=models.EmailField(max_length=250,blank=False)

    mdp=models.CharField(max_length=30,blank=False)
