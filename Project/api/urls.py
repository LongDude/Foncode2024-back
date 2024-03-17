from django.urls import path, include
from .views import UserViewset
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path('login/', UserViewset.as_view({'get': 'retrieve'})),
    path('register/', UserViewset.as_view({'post': 'create'}))
]
