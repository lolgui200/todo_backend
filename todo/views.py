from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo

from todo.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['NomPrenom']
    search_fields = ['NomPrenom']


