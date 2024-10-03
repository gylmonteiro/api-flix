from django.db.models import Sum, Avg
from rest_framework import serializers
from .models import Filme
from generos.models import Genero
from generos.serializers import GeneroSerializer
from atores.models import Ator
from atores.serializers import AtorSerializer


# Criamos este exemplo de um serializer manual. Ofertando maior poder de personalização
class FilmeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    titulo = serializers.CharField()
    genero = serializers.PrimaryKeyRelatedField(queryset=Genero.objects.all())
    ano_de_lancamento = serializers.IntegerField()
    atores = serializers.PrimaryKeyRelatedField(queryset=Ator.objects.all(), many=True)
    resumo = serializers.CharField()

    def create(self, validated_data):
        todos_atores = validated_data.pop("atores")

        filme = Filme.objects.create(**validated_data)
        filme.atores.set(todos_atores)
        return filme


class FilmeListSerializer(serializers.ModelSerializer):
    media_avaliacao = serializers.SerializerMethodField(read_only=True)
    genero = GeneroSerializer()
    atores = AtorSerializer(many=True)

    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'media_avaliacao','genero', 'atores', 'ano_de_lancamento', 'resumo']

    def get_media_avaliacao(self, instance):
        """
        # Fazendo a média com base na soma de avaliações e depois dividindo pela quantidade de avaliações

        soma_avaliacoes = instance.avaliacoes.aggregate(valor_total=Sum('estrelas'))['valor_total']
        quantidade_avaliacoes = instance.avaliacoes.all().count()
        """

        """
        if quantidade_avaliacoes == 0:
            return "Filme ainda não recebeu avaliações. Seja o primeiro a avaliar"        
        elif media_avaliacoes is not None:
            return media_avaliacoes
        """

        # FAzendo a média com a função Avg
        media_avaliacoes = instance.avaliacoes.aggregate(valor_medio=Avg("estrelas"))[
            "valor_medio"
        ]

        if media_avaliacoes:
            return round(media_avaliacoes, 1)

        return None


# Serializador com model
class FilmeModelSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Filme
        fields = "__all__"

    

    # Uma validação de ano de lançamento
    def validate_ano_de_lancamento(self, value):

        if value < 2000:
            raise serializers.ValidationError("Não pode cadastrar menor de 2000")
        return value

    # Uma nova validação
    def validate_resumo(self, value):
        if len(value) > 150:
            raise serializers.ValidationError(
                "Não pode cadastrar com mais de 150 caracteres o resumo"
            )
        return value
