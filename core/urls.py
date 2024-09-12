
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('generos/', include('generos.urls')),
    path('atores/', include('atores.urls')),
    path('filmes/', include('filmes.urls')),
    path('avaliacoes/', include('avaliacoes.urls'))
]
