from .models import Usuario, Imovel, Contrato, Pagamento
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    