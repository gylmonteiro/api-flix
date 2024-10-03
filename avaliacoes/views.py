from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Avaliacao
from .serializers import AvaliacaoSerializer


# Create your views here.


class AvaliacaoListaCriaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
