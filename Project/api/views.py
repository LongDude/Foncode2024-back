from django.shortcuts import render
from rest_framework.views import APIView

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