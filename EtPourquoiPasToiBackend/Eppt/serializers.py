#Convertir la data dans le format JSON

import email
from rest_framework import serializers
from Eppt.models import Temoignages,Utilisateurs


class TemoignageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Temoignages
        fields=('temoignageId','titre','datePublication','domaineEtude','typeTemoignage','region','contenu','utilisateurId')

class UtilisateurSerializer(serializers.ModelSerializer):

    password2= serializers.CharField(style={'input_type':'password'},write_only=True) #création du mdp2 qui est au même format que 'password' qui existe déjà dans l'AbstractBaseUser 

    class Meta:
        model=Utilisateurs
        fields=('nom','prenom','typeUtilisateur','email','password','password2')
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        utilisateur=Utilisateurs(email=self.validated_data['email']) #vérification que l'email n'est pas déjà dans la bdd
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2: #Vérification si les mdp sont différents 
            raise serializers.ValidationError({'password':'Les mots de passe ne correspondent pas' })
        utilisateur.set_password(password)
        utilisateur.save()
        return utilisateur

