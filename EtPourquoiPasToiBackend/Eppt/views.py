from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Eppt.models import Temoignages, Utilisateurs
from Eppt.serializers import TemoignageSerializer, UtilisateurSerializer

#Création des GET, POST, PUT, DELETE du modèle témoignage

@api_view(['GET',])
def temoignageDetails(request,temoignageId):
    try :
        temoignage=Temoignages.objects.get(temoignageId=temoignageId)
    except Temoignages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        temoignage_serializer=TemoignageSerializer(temoignage)
        return Response(temoignage_serializer.data)


@api_view(['PUT',])
def temoignageModification(request,temoignageId):
    try :
        temoignage=Temoignages.objects.get(temoignageId=temoignageId)
    except Temoignages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="PUT":
        temoignage_serializer=TemoignageSerializer(temoignage,data=request.data)
        data={}
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            data["succes"]="La modification a bien été prise en compte !"
            return Response(data=data)
        return Response(temoignage_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def temoignageSuppression(request,temoignageId):
    try :
        temoignage=Temoignages.objects.get(temoignageId=temoignageId)
    except Temoignages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="DELETE":
        operation=temoignage.delete()
        data={}
        if operation:
            data["succes"]="La suppression a bien été effectuée !"
        else:
            data["echec"]="La supression a échoué !"
        return Response(data=data)


@api_view(['POST',])
def temoignageCreation(request):
    utilisateur=Utilisateurs.objects.get(pk=1)
    temoignage=Temoignages(utilisateurId=utilisateur)
   
    if request.method=="POST":
        temoignage_serializer=TemoignageSerializer(temoignage,data=request.data)
        data={}
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            return Response(temoignage_serializer.data,status=status.HTTP_201_CREATED)
        return Response(temoignage_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        



#Création des GET, POST, PUT, DELETE du modèle utilisateurs

@api_view(['POST',])
def inscription(request):

    if request.method=='POST':
        utilisateur_serializer=UtilisateurSerializer(data=request.data)
        data={}
        if utilisateur_serializer.is_valid():
            utilisateur=utilisateur_serializer.save()
            data['reponse']="La création du compte a été effectué !"
            data['email']=utilisateur.email
            token=Token.objects.get(user=utilisateur).key
            data['token']=token
        else :
            data=utilisateur_serializer.errors
        return Response(data)

     


