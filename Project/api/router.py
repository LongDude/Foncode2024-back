from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

# работа с пользователем
router.register(r"register", UserViewset, basename="register-user")
#router.register(r"login", UserViewset)

# работа с курсом
#router.register(r"courses", CourseViewset)
#router.register(r"content", ContentViewset)

# добавление эоементов
#router.register(r"add_course", CourseViewset)
#router.register(r"add_content", ContentViewset)

urlpatterns = router.urls
