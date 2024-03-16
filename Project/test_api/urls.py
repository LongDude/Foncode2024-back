from django.urls import path, include
from test_api.views import TodoListAppView

urlpatterns = [
    path('api', TodoListAppView.as_view()),
]