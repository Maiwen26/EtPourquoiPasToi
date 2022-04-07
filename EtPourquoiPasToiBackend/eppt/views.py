from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Temoignage
from .serializers import TemoignageSerializer

# Create your views here.

class TemoignageListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    # 1. List all  PB Avec région
    #def get(self, request, *args, **kwargs):
    #    '''
     #   List all the temoignage items for given requested user
     #   '''
    #    temoignage = Temoignage.objects.filter(region = request.data.region)
    #    serializer = TemoignageSerializer(temoignage, many=True)
     #   return Response(serializer.data, status=status.HTTP_200_OK)

    
    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Temoignage with given témoignage data
        '''
        data = {
            'titreTemoignage': request.data.get('titreTemoignage'), 
            'typeTemoignage':request.data.get('typeTemoignage'),
            'contenu': request.data.get('contenu'), 
            'region': request.data.get('region'),
            'domaineEtude':request.data.get('domaineEtude'),
        }
        serializer = TemoignageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TemoignageDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, temoignage_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Temoignage.objects.get(id=temoignage_id, user = user_id)
        except Temoignage.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, temoignage_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        temoignage_instance = self.get_object(temoignage_id, request.user.id)
        if not temoignage_instance:
            return Response(
                {"res": "Object with temoignage id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TemoignageSerializer(temoignage_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, temoignage_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        temoignage_instance = self.get_object(temoignage_id, request.user.id)
        if not temoignage_instance:
            return Response(
                {"res": "Object with temoignage id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titreTemoignage': request.data.get('titreTemoignage'), 
            'typeTemoignage':request.data.get('typeTemoignage'),
            'contenu': request.data.get('contenu'), 
            'region': request.data.get('region'),
            'domaineEtude':request.data.get('domaineEtude'),
        }
        serializer = TemoignageSerializer(instance = temoignage_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, temoignage_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        temoignage_instance = self.get_object(temoignage_id, request.user.id)
        if not temoignage_instance:
            return Response(
                {"res": "Object with temoignage id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        temoignage_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



