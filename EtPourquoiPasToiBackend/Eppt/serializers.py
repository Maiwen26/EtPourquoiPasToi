from pyexpat import model
from rest_framework import serializers
from Eppt.models import Temoignages,Utilisateurs


class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Temoignages
        fields=('temoignageId','titre','datePublication','domaineEtude','typeTemoignage','region','contenu','utilisateurId')

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Utilisateurs
        fields=('utilisateurId','nom','prenom','email','typeUtilisateur','region','contenu','utilisateurId')
