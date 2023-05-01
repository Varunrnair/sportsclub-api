from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterAPI.as_view(),name='register'),
	path('login/',views.LoginAPI.as_view(),name='login'),
    path('display/',views.display.as_view(),name='display'),
    path('player/', views.PlayerList.as_view(), name="players"),
    path('managers/', views.ManagerList.as_view(), name="players"),
    path('referees/', views.RefereeList.as_view(), name="players"),
    path('owner/', views.OwnerList.as_view(), name="owners"),
]