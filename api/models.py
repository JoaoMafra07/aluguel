from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    telefone = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=20)

class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    locador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imovel = models.ForeignKey(Imovel, on_delete=models.SET_NULL, null=True)
    locador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='alugueis')
    locatario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='locacoes')

class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
