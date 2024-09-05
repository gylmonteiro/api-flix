from django.urls import path
from . import views



urlpatterns = [
    path("", views.generos_view, name='lista-generos'),
]
