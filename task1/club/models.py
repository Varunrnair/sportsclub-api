from django.db import models
from users.models import *
from django.conf import settings

class Competition(models.Model):
    com_name       = models.CharField(max_length= 200, primary_key=True)
    com_winner     = models.CharField(max_length=200, default="no winners")
    
    def __str__(self):
        return self.com_name


class Manager(models.Model):
    manager = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Referee(models.Model):
    referee = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Footballclub(models.Model):
    fc_id          = models.IntegerField(primary_key=True)
    club_logo      = models.CharField(max_length=240)
    fc_name        = models.CharField(max_length=255)
    description    = models.TextField(default="") 
    fc_email       = models.EmailField() 
    fc_stadium     = models.TextField(default="")  
    fc_location    = models.TextField(default="") 
    position       = models.IntegerField()
    competing      = models.ForeignKey(Competition,related_name="compi", on_delete=models.CASCADE)
    managers       = models.ForeignKey(Manager, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return self.fc_name


class Match(models.Model):
    match_timing   = models.TextField(default="")
    match_location = models.TextField(primary_key=True)  
    playedby       = models.ForeignKey(Footballclub, on_delete=models.CASCADE)
    refereed_by    = models.ForeignKey(Referee, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.match_location


class Player(models.Model):
    player = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    jersey = models.IntegerField()
    coach = models.OneToOneField(Manager, on_delete=models.CASCADE, default="")
    

