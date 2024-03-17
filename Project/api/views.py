from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserAPI(APIView):

    def get(self, request):
        ''' get user by id'''
        try:
            user_id = request.data.get('name')
            user = User.objects.get(name=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        usr_ser = UserSerializer(data=user)
        if usr_ser.is_valid():
            return Response(usr_ser.data, status=status.HTTP_200_OK)
        return Response(usr_ser.errors, status=status.HTTP_400_BAD_REQUEST)

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
    queryset = User.objects.all()

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
    
    def retrieve(self, request, pk=None):
        print("retrieve user")
        print(request.query_params)

        login = request.query_params["login"]        
        users = User.objects.filter(login=login)
        print(login, users)
        user = get_object_or_404(users)
        serializer = UserSerializer(user)
        return Response(serializer.data)

