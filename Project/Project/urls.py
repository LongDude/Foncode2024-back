
from django.contrib import admin
from django.urls import path, include
from test_api import urls as test_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('test/', include(test_urls)),
]
