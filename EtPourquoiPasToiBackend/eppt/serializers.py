from rest_framework import serializers
from eppt.models import Utilisateur,Temoignage

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Utilisateur
        fields=('id','prenom','nom','email','mdp','typeUtilisateur')

class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Temoignage
        fields=('id','titreTemoignage','typeTemoignage','contenu','region','domaineEtude','datePublication')
