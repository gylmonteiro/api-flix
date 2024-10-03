from django.db.models import Count
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from .models import Filme
from .serializers import FilmeModelSerializer, FilmeListSerializer, FilmeSerializer
from core.permissions import GlobalPermissionClass
from .permissions import FilmePermissionClass

# Create your views here.


class FilmeListaCriaView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Filme.objects.all()
    # serializer_class = FilmeModelSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FilmeListSerializer
        return FilmeModelSerializer


class FilmeDetalhaAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer


class FilmesEstatisticasView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    queryset = Filme.objects.all()

    def get(self, request):
        total_filmes = self.queryset.count()
        filmes_por__genero = self.queryset.values("genero__nome").annotate(
            count=Count("id")
        )

        return response.Response(
            {
                "filmes_por_Genero": filmes_por__genero,
                "filmes_na_base_de_dados": total_filmes,
            },
            status=status.HTTP_200_OK,
        )
