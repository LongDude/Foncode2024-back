
from django.contrib import admin
from django.urls import path, include

from api import urls as api_urls
from api import router as router_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router_urls))
]
