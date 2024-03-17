from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

class UserAPI(APIView):

    def get(self, request):
        ''' get user by id'''
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(UserSerializer(data=user), status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'patronymic': request.data.get('patronymic')
        }
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .serializers import *

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print('create user')
        
        name = request.data.get('name')
        password = request.data.get('password')

        user = User.objects.filter(
            name=name).first()
        # if exists
        if user:
            return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)
        else:
            newUser = User(
                name=name, password=password)
            newUser.save()
            return Response(self.get_serializer(newUser).data, status=status.HTTP_201_CREATED)