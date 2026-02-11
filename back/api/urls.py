from django.urls import path
from .views import (
    UsuarioListCreateAPIView,
    UsuarioDetailView,
    listar_criar_usuario,
    ImovelListCreateAPIView,
    ImovelDetailView,
    listar_criar_imovel,
    ContratoListCreateAPIView,
    ContratoDetailView,
    listar_criar_contrato,
    PagamentoListCreateAPIView,
    PagamentoDetailView,
    listar_criar_pagamento
)

urlpatterns = [
    path('usuarios/', UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>/', UsuarioDetailView.as_view()),

    path('imoveis/', ImovelListCreateAPIView.as_view()),
    path('imovel/<int:pk>/', ImovelDetailView.as_view()),

    path('contratos/', ContratoListCreateAPIView.as_view()),
    path('contrato/<int:pk>/', ContratoDetailView.as_view()),

    path('pagamentos/', PagamentoListCreateAPIView.as_view()),
    path('pagamento/<int:pk>/', PagamentoDetailView.as_view()),

    path('users/', listar_criar_usuario),
    path('propertys/', listar_criar_imovel),
    path('contracts/', listar_criar_contrato),
    path('payments/', listar_criar_pagamento),
]
