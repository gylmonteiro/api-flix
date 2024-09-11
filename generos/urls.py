from django.urls import path
from . import views


urlpatterns = [
    path("", views.GeneroCreateListView.as_view(), name="cria-lista-generos"),
    path("<int:pk>/", views.GeneroDetalhaAtualizaDeletaView.as_view(), name="detalha-atualiza-genero"),
]
