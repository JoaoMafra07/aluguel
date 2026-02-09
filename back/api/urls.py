from django.urls import path
from .views import (
    UsuarioListCreateAPIView,
    UsuarioUpdateDestroyView,
    listar_criar_usuario,
    ImovelListCreateAPIView,
    ImovelUpdateDestroyView,
    listar_criar_imovel,
    ContratoListCreateAPIView,
    ContratoUpdateDestroyView,
    listar_criar_contrato,
    PagamentoListCreateAPIView,
    PagamentoUpdateDestroyView,
    listar_criar_pagamento
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>/', UsuarioUpdateDestroyView.as_view()),
    path('users/', listar_criar_usuario),

    path('imoveis/', ImovelListCreateAPIView.as_view()),
    path('imovel/<int:pk>/', ImovelUpdateDestroyView.as_view()),
    path('propertys/', listar_criar_imovel),

    path('contratos/', ContratoListCreateAPIView.as_view()),
    path('contrato/<int:pk>/', ContratoUpdateDestroyView.as_view()),
    path('contracts/', listar_criar_contrato),

    path('pagamentos/', PagamentoListCreateAPIView.as_view()),
    path('pagamento/<int:pk>/', PagamentoUpdateDestroyView.as_view()),
    path('payments/', listar_criar_pagamento),
]
