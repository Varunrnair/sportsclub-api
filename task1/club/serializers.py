from rest_framework import serializers
from .models import *
from users.models import *
from users.serializers import *
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class FootballclubSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Footballclub
        fields = '__all__'

    def get_status(self,obj):
        if obj.position < 2:
            return "Amazing"
        else :
            if obj.position  <18:
                return "Good, do better"
            else:
                return "Relegated"   
                

class CompetitionSerializer(serializers.ModelSerializer):
    compi = FootballclubSerializer(many =True)

    def create(self):
        footballclub = Footballclub.objects.create()
        for compi_data in compi_data:
            Competition.objects.create(footballclub=footballclub, compi=compi_data)
        return footballclub

    class Meta:
        model = Competition
        fields = ['com_name','com_winner', 'compi']


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

