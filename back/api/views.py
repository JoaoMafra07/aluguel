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

################ GENERICS (CLASSES) ################

# Usuario
# class UsuarioListCreateAPIView(ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class UsuarioDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# Imovel
class ImovelListCreateAPIView(ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ImovelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

# Contrato
class ContratoListCreateAPIView(ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

# Pagamento
class PagamentoListCreateAPIView(ListCreateAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class PagamentoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer


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
class UsuarioListCreateAPIView(APIView):
    
    def get(self, request):
        usuarios = Usuario.object.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetailView(APIView):

    def get_object(self, pk):
        return Usuario.objects.get(pk=pk)
    
    def get(self, request, pk):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    # Próxima aula: PUT e DELETE