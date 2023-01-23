from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ToySerializer
from .models import Toy


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
