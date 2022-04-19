from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Eppt.models import Temoignages,Utilisateurs
from Eppt.serializers import TemoignageSerializer,UtilisateurSerializer


#Création des GET, POST, PUT, DELETE du modèle témoignage

@csrf_exempt
def temoignageAPI(request, id=0):
    if request.method=='GET':
        temoignages=Temoignages.objects.all()
        temoignages_serializer=TemoignageSerializer(temoignages,many=True)
        return JsonResponse(temoignages_serializer.data,safe=False)
    
    elif request.method=='POST':
        temoignage_data=JSONParser().parse(request)
        temoignage_serializer=TemoignageSerializer(data=temoignage_data)
        if temoignage_serializer.is_valid():
            temoignage_serializer.save()
            return JsonResponse("Le témoignage a bien été ajouté !",safe=False)
        return JsonResponse("Le témoignage n'a pas pu être ajouté !",safe=False)
    
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
            return JsonResponse("Votre compte a bien été créé !",safe=False)
        return JsonResponse("Votre compte n'a pas pu être créé !",safe=False)
    
        


