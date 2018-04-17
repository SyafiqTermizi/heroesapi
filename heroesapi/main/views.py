from rest_framework import generics
from rest_framework import viewsets

from .models import Hero
from .serializers import HeroSerializers


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers
