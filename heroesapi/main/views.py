from rest_framework import generics

from django.shortcuts import render
from django.http import Http404

from .models import Hero
from .serializers import HeroSerializers


class HeroList(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers


class HeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers
