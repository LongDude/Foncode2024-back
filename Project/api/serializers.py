from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "surname", "patronymic", "group_name", "group_id", "VK_ID", "role_id", "password", "login"]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ["name", "description"]

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = ["name", "year"]

class FaculitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculity
        fields=["name"]
