from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Filme
from .serializers import FilmeModelSerializer, FilmeSerializer
from .permissions import FilmePermissionClass

# Create your views here.


class FilmeListaCriaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, FilmePermissionClass)
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer


class FilmeDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer
