
from django.contrib.auth.models import User
from rest_framework import serializers
from user_management.models import TodoUserProfile


class TodoUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
            model = TodoUserProfile
            fields = ('__all__')




class UserSerializer(serializers.ModelSerializer):
    
    profile = TodoUserProfileSerializer(source='todouserprofile')
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'user_permissions', 'profile')
