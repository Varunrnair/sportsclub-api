from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

class CompetitionList(APIView):
    def get(self, request, format=None):
        queryset = Competition.objects.all()
        serializer = CompetitionSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
            queryset=request.data
            com_name = queryset.get('com_name')    
            queryset = Competition.objects.all()
            queryset.delete()
            return Response(queryset.data)

class FootballclubList(APIView):
    def get(self, request, format=None):
        queryset = Footballclub.objects.all()
        serializer = FootballclubSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = FootballclubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        queryset=request.data
        queryset = Footballclub.objects.all()
        queryset.delete()
        return Response(queryset.data)

class MatchList(APIView):
    def get(self, request, format=None):
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#def index(request):
    #client = razorpay.Client(auth=(" ", " "))
    #amount : 1000
    #currency : 'INR'
    #payment = client.order.create({'amount':amount, 'currency':currency})
    #return render(request)