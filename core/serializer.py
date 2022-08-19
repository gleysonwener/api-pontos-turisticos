from rest_framework.serializers import ModelSerializer
from . models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'descricao', 'aprovado', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'foto',)