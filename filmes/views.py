from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Filme
from .serializers import FilmeModelSerializer, FilmeSerializer
from core.permissions import GlobalPermissionClass
from .permissions import FilmePermissionClass

# Create your views here.


class FilmeListaCriaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer


class FilmeDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer
