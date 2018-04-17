from rest_framework.routers import DefaultRouter

from django.urls import path, include
from django.conf.urls import url
from . import views


router = DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
