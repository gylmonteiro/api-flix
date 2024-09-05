from django.urls import path
from . import views



urlpatterns = [
    path("", views.generos_view, name='cria-lista-generos'),
    path("<int:pk>", ..., name='detalha-genero'),
]
