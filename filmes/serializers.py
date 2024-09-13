from rest_framework import serializers
from .models import Filme
from generos.models import Genero
from atores.models import Ator

#Criamos este exemplo de um serializer manual. Ofertando maior poder de personalização
class FilmeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField()
    genero = serializers.PrimaryKeyRelatedField(queryset = Genero.objects.all())
    ano_de_lancamento = serializers.IntegerField()
    atores = serializers.PrimaryKeyRelatedField(queryset = Ator.objects.all(), many=True)
    resumo = serializers.CharField()
    
    def create(self, validated_data):
        todos_atores = validated_data.pop('atores')
    
        filme = Filme.objects.create(**validated_data)
        filme.atores.set(todos_atores)
        return filme



class FilmeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filme
        fields = '__all__'

    def validate_ano_de_lancamento(self, value):

        if value < 2000:
            raise serializers.ValidationError("Não pode cadastrar menos de 2000")
        return value