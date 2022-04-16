from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from eppt.models import Utilisateur,Temoignage
from eppt.serializers import UtilisateurSerializer,TemoignageSerializer

#Create your views here.

@csrf_exempt
def utilisateurAPI(request,id=0):
    if request.method=='GET':
        utilisateurs=Utilisateur.objects.all()
        utilisateurs_serializer=UtilisateurSerializer(utilisateurs,many=True)
        return JsonResponse(utilisateurs_serializer.data,safe=False)
    
    elif request.method=='POST':
        utilisateur_data=JSONParser().parse(request)
        utilisateur_serializer=UtilisateurSerializer(data=utilisateur_data)
        if utilisateur_serializer.is_valid():
            utilisateur_serializer.save()
            return JsonResponse('Ajout confirmé !',safe=False)
        return JsonResponse('Erreur avec l ajout',safe=False)
    
    elif request.method=='PUT':
        utilisateur_data=JSONParser().parse(request)
        utilisateur=Utilisateur.objects.get(UtilisateurId=utilisateur_data['UtilisateurId'])
        utilisateur_serializer=UtilisateurSerializer(utilisateur,data=utilisateur_data)
        if utilisateur_serializer.is_valid():
            utilisateur_serializer.save()
            return JsonResponse("Modification réussie",safe=False)
    
    elif request.method=='DELETE':
        utilisateur=Utilisateur.objects.get(UtilisateurId=id)
        utilisateur.delete()
        return JsonResponse("Suppression réussie",safe=False)

