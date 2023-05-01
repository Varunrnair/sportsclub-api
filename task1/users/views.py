from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated




#class send_otp_via_email():
    #send_mail(
    #'Testing mail',
    #'Here is the message.',
    #'vmailextra@gmail.com',
    #['varunrnair2002@gmail.com'],
    #fail_silently=False,
#)

# Register API
class RegisterAPI(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        user = User.objects.get(email = serializer.data['email'])
        token = Token.objects.get_or_create(user=user)
        return Response(token, status=status.HTTP_201_CREATED, safe=False)


class LoginAPI(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        if user:
            #serializer = self.serializer_class(user)
            token, k= Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response('Invalid Credentials', status=status.HTTP_404_NOT_FOUND)



class display(APIView):
    serializer_class=UserSerializer
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



class PlayerList(APIView):
    def get(self, request, format=None):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data, )
        
    def post(self, request, format=None):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        queryset=request.data
        queryset = Player.objects.all()
        queryset.delete()
        return Response(queryset.data)

class ManagerList(APIView):
    def get(self, request, format=None):
        queryset = Manager.objects.all()
        serializer = ManagerSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RefereeList(APIView):
    def get(self, request, format=None):
        queryset = Referee.objects.all()
        serializer = RefereeSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = RefereeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)