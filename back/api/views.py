from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Usuario,
    Imovel,
    Contrato,
    Pagamento
)
from rest_framework.decorators import api_view
from .serializers import (
    UsuarioSerializer, 
    ImovelSerializer, 
    ContratoSerializer,
    PagamentoSerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

################ ViewSet Classes ################
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuarioFilter

    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo')
    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)

    #     return self.queryset

class ImovelViewSet(ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ImovelFilter

    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     tipo = self.request.query_params.get('tipo').title()
    #     status = self.request.query_params.get('status').upper()

    #     if tipo:
    #         self.queryset = self.queryset.filter(tipo=tipo)

    #     if status:
    #         self.queryset = self.queryset.filter(status=status)

    #     return self.queryset

class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = ContratoFilter

    # permission_classes = [IsAuthenticated]

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = PagamentoFilter

    # permission_classes = [IsAuthenticated]

################ GENERICS (CLASSES) ################

# Usuario
# class UsuarioListCreateAPIView(ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# Imovel
# class ImovelListCreateAPIView(ListCreateAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# class ImovelDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Imovel.objects.all()
#     serializer_class = ImovelSerializer

# Contrato
# class ContratoListCreateAPIView(ListCreateAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# class ContratoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Contrato.objects.all()
#     serializer_class = ContratoSerializer

# # Pagamento
# class PagamentoListCreateAPIView(ListCreateAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

# class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Pagamento.objects.all()
#     serializer_class = PagamentoSerializer

################ DECORATORS (FUNÇÕES) ################

@api_view(['GET', 'POST'])
def listar_criar_usuario(request):
    if request.method == 'GET':
        queryset = Usuario.objects.all()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 

            return Response({"Mensagem": "Usuário criado com sucesso"}, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listar_criar_imovel(request):
    if request.method == 'GET':
        queryset = Imovel.objects.all()
        serializer = ImovelSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ImovelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 

            return Response({"Mensagem": "Imóvel criado com sucesso"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listar_criar_contrato(request):
    if request.method == 'GET':
        queryset = Contrato.objects.all()
        serializer = ContratoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ContratoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 

            return Response({"Mensagem": "Contrato criado com sucesso"}, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def listar_criar_pagamento(request):
    if request.method == 'GET':
        queryset = Pagamento.objects.all()
        serializer = PagamentoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PagamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 

            return Response({"Mensagem": "Pagamento criado com sucesso"}, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
############################################ Via APIView ############################################
# class UsuarioListCreateAPIView(APIView):
    
#     def get(self, request):
#         usuarios = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuarios, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UsuarioSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UsuarioDetailView(APIView):

#     def get_object(self, pk):
#         return Usuario.objects.get(pk=pk)
    
#     def delete(self, request, pk):
#         usuario = self.get_object(pk)
#         usuario.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         usuario = self.get_object(pk)
#         serializer = UsuarioSerializer(usuario, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ImovelListCreateAPIView(APIView):
#     def get(self, request):
#         imoveis = Imovel.objects.all()
#         serializer = ImovelSerializer(imoveis, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ImovelSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ImovelDetailView(APIView):
#     def get_object(self, pk):
#         return Imovel.objects.get(pk=pk)
    
#     def delete(self, request, pk):
#         imovel = self.get_object(pk)
#         imovel.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         imovel = self.get_object(pk)
#         serializer = ImovelSerializer(imovel, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
# class ContratoListCreateAPIView(APIView):
#     def get(self, request):
#         contratos = Contrato.objects.all()
#         serializer = ContratoSerializer(contratos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ContratoSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ContratoDetailView(APIView):
#     def get_object(self, pk):
#         return Contrato.objects.get(pk=pk)
    
#     def delete(self, request, pk):
#         contrato = self.get_object(pk)
#         contrato.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         contrato = self.get_object(pk)
#         serializer = ContratoSerializer(contrato, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PagamentoListCreateAPIView(APIView):
#     def get(self, request):
#         pagamentos = Pagamento.objects.all()
#         serializer = PagamentoSerializer(pagamentos, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PagamentoSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PagamentoDetailView(APIView):
#     def get_object(self, pk):
#         return Pagamento.objects.get(pk=pk)
    
#     def delete(self, request, pk):
#         pagamento = self.get_object(pk)
#         pagamento.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         pagamento = self.get_object(pk)
#         serializer = PagamentoSerializer(pagamento, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

