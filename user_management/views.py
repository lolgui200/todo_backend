from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from user_management.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MeViewSet(viewsets.ViewSet): 
    
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)