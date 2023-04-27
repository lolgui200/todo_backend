from django.db import models
from user_management.models import TodoUserProfile
class Todo(models.Model):
    profile = TodoUserProfile
    SEXE = [
      ("hongre","hongre"),
      ("étalon","étalon"),
      ("jument","jument"),
    ]
    NomPrenom = models.CharField(max_length=255)
    NomProp = models.CharField(max_length=255)
    Puce = models.CharField(max_length=255)

    sexe = models.CharField(max_length=10, choices=SEXE)
    poney = models.BooleanField()
    UELN = models.CharField(max_length=255)
    DTN = models.DateField()
    IMA = models.CharField(max_length=50)
    Note = models.CharField(max_length=255)
    




