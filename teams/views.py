from django.shortcuts import render
from rest_framework import generics
from .models import Team
from .serializers import *

# Create your views here.
class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all().order_by('team_name')
    serializer_class = TeamSerializer

class TeamCreateAPIView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamUpdateAPIView(generics.UpdateAPIView, generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'

class DestroyAPIView(generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'id'



