from rest_framework import generics
from .models import Avaliacao
from .serializers import AvaliacaoSerializer


# Create your views here.

class AvaliacaoListaCriaView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    