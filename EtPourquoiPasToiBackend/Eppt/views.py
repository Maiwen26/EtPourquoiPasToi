
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter

from Eppt.models import Temoignages, Utilisateurs
from Eppt.serializers import TemoignageSerializer, InscriptionSerializer, CompteUtilisateurSerializer

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
@permission_classes((IsAuthenticated,))
def temoignageModification(request,temoignageId):
    try :
        temoignage=Temoignages.objects.get(temoignageId=temoignageId)
    except Temoignages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    utilisateur=request.utilisateur
    if temoignage.utilisateurId!=utilisateur.utilisateurId:
        return Response({'reponse':"Vous ne pouvez pas faire cette action !"})
    
    if request.method=="PUT":
        temoignage_serializer=TemoignageSerializer(temoignage,data=request.data)
        data={}
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            data["succes"]="La modification a bien été prise en compte !"
            return Response(data=data)
        return Response(temoignage_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def temoignageSuppression(request,temoignageId):
    try :
        temoignage=Temoignages.objects.get(temoignageId=temoignageId)
    except Temoignages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    utilisateur=request.utilisateur
    if temoignage.utilisateurId!=utilisateur.utilisateurId:
        return Response({'reponse':"Vous ne pouvez pas faire cette action !"})
    

    if request.method=="DELETE":
        operation=temoignage.delete()
        data={}
        if operation:
            data["succes"]="La suppression a bien été effectuée !"
        else:
            data["echec"]="La supression a échoué !"
        return Response(data=data)


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def temoignageCreation(request):
    utilisateur=Utilisateurs.objects.get(utilisateurId=1)
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
        utilisateur_serializer=InscriptionSerializer(data=request.data)
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

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def vueProfil(request):
    try:
        utilisateur=request.utilisateur
    except Utilisateurs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=CompteUtilisateurSerializer(utilisateur)
        return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def modificationProfil(request):
    try:
        utilisateur=request.utilisateur
    except Utilisateurs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='PUT':
        serializer=CompteUtilisateurSerializer(utilisateur,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response']="Modification de vos informations réuissie !"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def suppressionProfil(request,utilisateurId):
    try :
        utilisateur=Utilisateurs.objects.get(utilisateurId=utilisateurId)
    except Utilisateurs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    utilisateur2=request.utilisateur
    if utilisateur2.utilisateurId!=utilisateur.utilisateurId:
        return Response({'reponse':"Vous ne pouvez pas faire cette action !"})
    

    if request.method=="DELETE":
        operation=utilisateur.delete()
        data={}
        if operation:
            data["succes"]="La suppression a bien été effectuée !"
        else:
            data["echec"]="La supression a échoué !"
        return Response(data=data)


#Création de la vue comprenant la liste de tous les témoignages présents dans la bdd   
class ListeTemoignage(ListAPIView):
    queryset=Temoignages.objects.all()
    serializer_class=TemoignageSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    pagination_class=PageNumberPagination
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('domaineEtude')


