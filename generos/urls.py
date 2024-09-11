from django.urls import path
from . import views


urlpatterns = [
    path("", views.GeneroCreateListView.as_view(), name="cria-lista-generos"),
    path("<int:pk>/", views.view_detalhar__atualizar_genero, name="detalha-atualiza-genero"),
]
