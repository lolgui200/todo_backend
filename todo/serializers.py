from rest_framework import serializers

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    Date_de_naissance = serializers.DateField(source='DTN')
    Nom_du_propiétaire = serializers.CharField(source='NomProp')
    

    class Meta:
        model = Todo
        exclude = ('DTN', 'NomProp')
        



