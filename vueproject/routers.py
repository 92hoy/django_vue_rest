from rest_framework import routers
from vueapp.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'vueapp', UserViewSet)