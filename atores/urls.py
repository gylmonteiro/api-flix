from django.urls import path
from . import views


urlpatterns = [
    path("atores/", views.AtorListaCriaView.as_view(), name="lista-cria-atores"),
    path(
        "atores/<int:pk>/",
        views.AtorDetalhaAtualizaDeletaView.as_view(),
        name="detalha-atualiza-deleta-atores",
    ),
]
