from django.urls import path
from . import views



urlpatterns = [
    path("", views.generos_view, name='cria-lista-generos'),
    path("<int:pk>/", views.detalhar_genero_view, name='detalha-genero'),
]
