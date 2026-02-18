from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'imoveis', ImovelViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'pagamentos', PagamentoViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresh serve para, depois de um determinado período de tempo de inatividade no programa, é solicitado recadastro.

    path('', include(router.urls)), #ViewSet

    path('users/', listar_criar_usuario), #Decorator APIView
    path('propertys/', listar_criar_imovel), #Decorator APIView
    path('contracts/', listar_criar_contrato), #Decorator APIView
    path('payments/', listar_criar_pagamento), #Decorator APIView

    # path('usuarios/', UsuarioListCreateAPIView.as_view()),
    # path('usuario/<int:pk>/', UsuarioDetailView.as_view()),

    # path('imoveis/', ImovelListCreateAPIView.as_view()),
    # path('imovel/<int:pk>/', ImovelDetailView.as_view()),

    # path('contratos/', ContratoListCreateAPIView.as_view()),
    # path('contrato/<int:pk>/', ContratoDetailView.as_view()),

    # path('pagamentos/', PagamentoListCreateAPIView.as_view()),
    # path('pagamento/<int:pk>/', PagamentoDetailView.as_view()),
]
