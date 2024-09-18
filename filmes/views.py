from rest_framework import generics
from .models import Filme
from .serializers import FilmeModelSerializer, FilmeSerializer

# Create your views here.


class FilmeListaCriaView(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer


class FilmeDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer