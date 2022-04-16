from rest_framework import serializers
from .models import Temoignage

class TemoignageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Temoignage
        fields=('titreTemoignage','typeTemoignage','datePublication','contenu','region','domaineEtude')
