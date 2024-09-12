from rest_framework import generics
from .models import Filme
from .serializers import FilmeSerializer

# Create your views here.


class FilmeListaCriaView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer