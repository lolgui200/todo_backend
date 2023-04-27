from django.db import models
from django.contrib.auth.models import User
  
class TodoUserProfile(models.Model):
    
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=15,null=False)
    adresse = models.CharField(max_length=255,null=False)
    TVA = models.CharField(max_length=50)
    nomMarch = models.CharField(max_length=100)
    telMARCH = models.CharField(max_length=15)
    nomVet = models.CharField(max_length=100)
    telMARCH = models.CharField(max_length=15)
