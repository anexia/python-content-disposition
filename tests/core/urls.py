from django.urls import include, path
from rest_framework import routers
from testapp.views import PhotoViewSet

router = routers.DefaultRouter()
router.register(r"photo", PhotoViewSet)

urlpatterns = [path("api/", include(router.urls))]
