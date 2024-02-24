# myapp/serializers.py
from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        # fields = ('id', 'team_name', 'image_id', 'event_name', 'description', 'date')
        fields = '__all__'
