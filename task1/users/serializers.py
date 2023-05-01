from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=32,min_length=8,write_only = True)
    
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password=serializers.CharField(max_length=32,min_length=8,write_only = True)
    
    class Meta:
        model  = User
        fields = ['email','password']


class OwnerSerializer(serializers.ModelSerializer):
    owner=serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='email'
    )
    class Meta:
        model = Owner
        fields = '__all__'
    def save(self):
        owner=self.validated_data['owner']
        index=Owner(
            owner=User.objects.get(email=owner)
        )
        index.save()


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