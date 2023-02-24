from django.urls import path
from . import views


urlpatterns = [
    path('competition/', views.CompetitionList.as_view(), name="competition"),
    path('footballclub/', views.FootballclubList.as_view(), name="footballclubs"),
    path('match/', views.MatchList.as_view(), name="matches"),
    path('player/', views.PlayerList.as_view(), name="players"),
    path('managers/', views.ManagerList.as_view(), name="players"),
    path('referees/', views.RefereeList.as_view(), name="players"),
]