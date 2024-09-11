from rest_framework import serializers
from .models import Genero

class GeneroListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = '__all__'
