from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Números não são permitidos no campo nome'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O campo RG deve ter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O número de celular deve seguir o modelo: 11 91234-1234'})
        return data
