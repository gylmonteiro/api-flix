from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("autenticacao/", TokenObtainPairView.as_view(), name="obtem-token"),
    path(
        "autenticacao/token/refresh/", TokenRefreshView.as_view(), name="atualiza-token"
    ),
    path(
        "autenticacao/token/verifica/", TokenVerifyView.as_view(), name="verifica-token"
    ),
]
