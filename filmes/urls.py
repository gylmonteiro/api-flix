from django.urls import path
from . import views


urlpatterns = [
    path("", views.FilmeListaCriaView.as_view(), name="lista-cria-filmes"),
    path("<int:pk>/", views.FilmeDetalhaAtualizaDeletaView.as_view(), name="detalha-atualiza-deleta-filme",
    ),
]
