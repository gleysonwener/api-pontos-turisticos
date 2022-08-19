from rest_framework.serializers import ModelSerializer
from . models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = '__all__'