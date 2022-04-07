from rest_framework import serializers
from .models import Temoignage

class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Temoignage
        fields=["titreTemoignage","typeTemoignage","datePublication","contenu","region","domaineEtude"]