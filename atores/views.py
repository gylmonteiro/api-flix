from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Ator
from .serializers import AtorSerializer

class AtorListaCriaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class AtorDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer