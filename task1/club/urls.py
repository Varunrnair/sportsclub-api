from django.urls import path
from . import views


urlpatterns = [
    path('competition/', views.CompetitionList.as_view(), name="competition"),
    path('footballclub/', views.FootballclubList.as_view(), name="footballclubs"),
    path('match/', views.MatchList.as_view(), name="matches"),
]