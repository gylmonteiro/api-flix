from rest_framework import generics
from .models import Ator
from .serializers import AtorSerializer

class AtorListaCriaView(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class AtorDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer