from .models import Usuario, Imovel, Contrato, Pagamento
from django.contrib.auth.models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RegisterSerializer(serializers.Serializer):
    #campos da tabela AUTH_USER
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    #campos da tabela Usuario
    nome = serializers.CharField(required=False, allow_blank=True, default="") # required por padrão já é False
    telefone = serializers.CharField(required=False, allow_blank=True, default="")
    tipo = serializers.ChoiceField(choices=Usuario.TIPO_CHOICES)

    def create(self, validated_data):
        nome = validated_data.get('nome', '')
        telefone = validated_data.get('telefone', '')
        tipo = validated_data['tipo'] # Está entre colchetes pq não eh um CharField
        email = validated_data['email']

        #Criando usuário na tabela auth_user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=email,
            password=validated_data['password']
        )

        if tipo == 'LOCADOR':
            user.is_staff = True
        else:
            user.is_staff = False
            
        user.is_active = True
        user.is_superuser = False
        user.save()

        # Criando usuário na tabela Usuario
        Usuario.objects.create(
            user=user,
            nome=nome if nome else user.username,
            email=email,
            telefone=telefone,
            tipo=tipo
        )
    
        return user

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'
    
class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'