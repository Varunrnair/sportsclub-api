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

  
class ManagerSerializer(serializers.ModelSerializer):
    manager=serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='email'
    )

    class Meta:
        model = Manager
        fields = '__all__'

    def save(self):
        manager=self.validated_data['manager']
        index=Manager(
            manager=User.objects.get(email=manager)
        )
        index.save()


class RefereeSerializer(serializers.ModelSerializer):
    referee=serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='email'
    )
    class Meta:
        model = Referee
        fields = '__all__'
    def save(self):
        referee=self.validated_data['referee']
        index=Referee(
            referee=User.objects.get(email=referee)
        )
        index.save()


class PlayerSerializer(serializers.ModelSerializer):
    
    player=serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="email"
    )
    coach=serializers.SlugRelatedField(
        queryset=Manager.objects.all(),
        slug_field="manager"
    )

    class Meta:
        model = Player
        fields = '__all__'

    def save(self):
        coach=self.validated_data['coach']
        player=self.validated_data['player']
        index=Player(
            coach=Manager.objects.get(user=coach),
            player=User.objects.get(email=player)
        )
        index.save()

    '''def create(self):
        manager = Manager.objects.create()
        for player_data in player_data:
            Player.objects.create(player=player_data, manager=manager)
        return Manager'''