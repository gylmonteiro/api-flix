from django.urls import path
from . import views


urlpatterns = [
    path("", views.AtorListaCriaView.as_view(), name="lista-cria-atores"),
    path(
        "<int:pk>/",
        views.AtorDetalhaAtualizaDeletaView.as_view(),
        name="detalha-atualiza-deleta-atores",
    ),
]
