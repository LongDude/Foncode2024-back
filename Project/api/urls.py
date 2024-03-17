from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns=[
    path('login/', UserViewset.as_view({'get': 'retrieve'})),
    path('register/', UserViewset.as_view({'post': 'create'})),
    path('get_users/', get_users),
    path('get_group_users', get_group_users),
    path('get_facullity_groups', get_faculity_groups),
    path('get_faculity', get_faculity_list),
    path('register_user', register_user)
]
