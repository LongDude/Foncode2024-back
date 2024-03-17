from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


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
        print(request.data)

        login = request.data.get("login")
        
        users = User.objects.filter(name=name)
        user = get_object_or_404(users)
        serializer = UserSerializer(user)
        return Response(serializer.data)

