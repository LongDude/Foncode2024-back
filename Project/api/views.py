from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import User
from .models import *
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

@api_view(["POST"])
def register_user(request):
    user = User.objects.filter(login=request.data.get("login")).first()
    if user:
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    else:
        newUser = User(
            user
        )
        newUser.save()
        return Response(UserSerializer(newUser).data, status=status.HTTP_200_OK)

@api_view
def get_courses_byUser(request):
    couses = Course.objects.filter(id__user_course__user_id = request.user.id)
    serializer = CourceSerializer(couses, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view
def get_courses(request):
    couses = Course.objects.all()
    serializer = CourceSerializer(couses, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view
def get_course_content(request):
    content = Content.objects.filter(course_id=request.course.id).first()
    serializer = ContentSerializer(content)
    return Response(serializer.date, status=HTTP_200_OK)

@api_view(["GET"])
def get_faculity_list(request):
    faculityes = Faculity.objects.all()
    serializer = FaculitySerializer(faculityes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_faculity_groups(request):
    groups = Group.objects.filter(facility_id=request.faculity.id)
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_group_users(request):
    users = User.objects.filter(group_id=request.group.id)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
