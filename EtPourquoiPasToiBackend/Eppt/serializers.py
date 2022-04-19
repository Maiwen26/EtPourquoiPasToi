from rest_framework import serializers
from Eppt.models import Temoignages,Utilisateurs


class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Temoignages
        fields=('temoignageId','titre','datePublication','domaineEtude','typeTemoignage','region','contenu','utilisateurId')

