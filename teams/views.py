from django.shortcuts import render
from rest_framework import generics
from .models import Team
from .serializers import TeamSerializer

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all().order_by('team_name')
    serializer_class = TeamSerializer

class TeamCreateAPIView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# Create your views here.
