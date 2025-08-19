from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from backend.models import Categorie, Mission
from backend.serializers import CategorieSerializer, MissionSerializer

# Create your views here.


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello, Emmanuel!"})
    

class  MissionViewSet(viewsets.ModelViewSet):

    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class  CategorieViewSet(viewsets.ModelViewSet):

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

# class SignalementViewSet(viewsets.ModelViewSet):
#     queryset = Signalement.objects.all()
#     serializer_class = SignalementSerializer  