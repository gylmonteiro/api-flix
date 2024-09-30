from django.urls import path
from . import views


urlpatterns = [
    path("filmes/", views.FilmeListaCriaView.as_view(), name="lista-cria-filmes"),
    path("filmes/<int:pk>/", views.FilmeDetalhaAtualizaDeletaView.as_view(), name="detalha-atualiza-deleta-filme",
    ),
    path("filmes/estatisticas/", views.FilmesEstatisticasView.as_view(), name="estatisticas-filmes"),
]
