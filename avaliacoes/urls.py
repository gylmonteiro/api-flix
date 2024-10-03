from django.urls import path
from . import views


urlpatterns = [
    path(
        "avaliacoes/",
        views.AvaliacaoListaCriaView.as_view(),
        name="lista-cria-avaliacoes",
    ),
    path(
        "avaliacoes/<int:pk>/",
        views.AvaliacaoDetalhaAtualizaDeletaView.as_view(),
        name="detalha-atualiza-deleta-avaliacao",
    ),
]
