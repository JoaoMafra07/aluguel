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

################ GET E POST ################
class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Alternativa
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

################ UPDATE E DELETE ################
class UsuarioUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

################ GET E POST ################
class ImovelListCreateAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

# Alternativa
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

################ UPDATE E DELETE ################
class ImovelUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    
################ GET E POST ################
class ContratoListCreateAPIView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

# Alternativa
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

################ UPDATE E DELETE ################
class ContratoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    
################ GET E POST ################
class PagamentoListCreateAPIView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

# Alternativa
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

################ UPDATE E DELETE ################
class PagamentoUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    