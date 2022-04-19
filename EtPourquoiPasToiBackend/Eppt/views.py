from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pkg_resources import safe_extra
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Eppt.models import Temoignages
from Eppt.serializers import TemoignageSerializer


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


