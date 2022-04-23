from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Eppt.models import Temoignages, Utilisateurs
from Eppt.serializers import TemoignageSerializer

#Création des GET, POST, PUT, DELETE du modèle témoignage

@api_view(['GET',])
def temoignageDetails(request,slug):
    try :
        temoignage=Temoignages.objects.get(slug=slug)
    except Temoignages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        temoignage_serializer=TemoignageSerializer(temoignage)
        return Response(temoignage_serializer.data)


@api_view(['PUT',])
def temoignageModification(request,slug):
    try :
        temoignage=Temoignages.objects.get(slug=slug)
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
def temoignageSuppression(request,slug):
    try :
        temoignage=Temoignages.objects.get(slug=slug)
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
    temoignage=Temoignages(creatrice=utilisateur)
   
    if request.method=="POST":
        temoignage_serializer=TemoignageSerializer(temoignage,data=request.data)
        data={}
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            return Response(temoignage_serializer.data,status=status.HTTP_201_CREATED)
        return Response(temoignage_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        





















'''

@csrf_exempt
def temoignageAPI(request, id=0):
    if request.method=='GET':
        temoignages=Temoignages.objects.all()
        temoignages_serializer=TemoignageSerializer(temoignages,many=True)
        return Response(temoignages_serializer.data)
    
    elif request.method=='POST':
        temoignage_serializer=TemoignageSerializer(data=request.data)
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            return Response(temoignage_serializer.data)
        return Response(temoignage_serializer.errors)
    
    elif request.method=='PUT':
        temoignage_data=JSONParser().parse(request)
        temoignage=Temoignages.objects.get(temoignageId=temoignage_data['temoignageId'])
        temoignage_serializer=TemoignageSerializer(temoignage,data=temoignage_data)
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            return JsonResponse("Le témoignage a bien été modifié !",safe=False)
        return JsonResponse("Le témoignage n'a pas été modifié !",safe=False)

    elif request.method=='DELETE':
        temoignage=Temoignages.objects.get(temoignageId=id)
        temoignage.delete()
        return JsonResponse("Le témoignage a bien été supprimé !", safe=False)


#Création du POST de l'inscription

@csrf_exempt
def utilisateurAPI(request):
    if request.method=='POST':
        utilisateur_data=JSONParser().parse(request)
        utilisateur_serializer=UtilisateurSerializer(data=utilisateur_data)
        if utilisateur_serializer.is_valid():
            utilisateur_serializer.save()
           # utilisateur_serializer['token']=Token.objects.get(user=utilisateur_serializer).key
            return JsonResponse("Votre compte a bien été créé !",safe=False)
        return JsonResponse("Votre compte n'a pas pu être créé !",safe=False)
    
'''      


