import django_filters
from .models import *

class UsuarioFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name='nome', lookup_expr='icontains') #lookup_expr='icontains' vai filtrar por caracteres que estão presentes no nome. Se o usuário for João Mafra e eu procurar por 'Mafra', o usuário vai ser listado
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='iexact') #lookup_expr='iexact' vai filtrar por campos com a escrita idêntica à passada pelos parâmetros

    class Meta:
        models = Usuario
        fields = ['nome', 'tipo']

class ImovelFilter(django_filters.FilterSet):
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='iexact')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    valor_min = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='gte')
    valor_max = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='lte')

    class Meta:
        models = Imovel
        fields = ['tipo', 'status', 'valor_aluguel']

class ContratoFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='data_inicio', lookup_expr='gte')
    data_fim = django_filters.DateFilter(field_name='data_fim', lookup_expr='lte')
    valor_min = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='gte')
    valor_max = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='lte')

    class Meta:
        models = Contrato
        fields = ['data_inicio', 'data_fim', 'valor_aluguel']

class PagamentoFilter(django_filters.FilterSet):
    data_min = django_filters.DateFilter(field_name='data_inicio', lookup_expr='gte')
    data_max = django_filters.DateFilter(field_name='data_fim', lookup_expr='lte')
    valor_min = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='gte')
    valor_max = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='lte')

    class Meta:
        models = Imovel
        fields = ['data_inicio', 'data_fim', 'valor_aluguel']
# class PagamentoFilter(django_filters.FilterSet):
#     valor_aluguel = django_filters.NumberFilter(field_name='valor_aluguel', lookup_expr='gte')
#     data_pagamento = django_filters.DateFilter()