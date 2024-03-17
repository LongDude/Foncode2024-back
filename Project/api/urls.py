from django.urls import path, include
from .views import UserAPI
from .views import UserViewset
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path('user/', UserAPI.as_view()),
]
