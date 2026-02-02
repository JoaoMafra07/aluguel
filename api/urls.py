from django.urls import path
from .views import (
    UsuarioListCreateAPIView,
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view())
]