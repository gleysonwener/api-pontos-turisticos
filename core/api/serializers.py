from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework import serializers
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from rest_framework.fields import SerializerMethodField
from atracoes.models import Atracao
from enderecos.models import Endereco

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer(read_only=True)
    #comentarios = ComentarioSerializer(many=True, read_only=True)
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    descricao_completa = SerializerMethodField(read_only=True)

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'foto', 
        'descricao_completa','descricao_completa2',)
        read_only_fields = ('comentarios', 'avaliacoes',)

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validate_data):
        atracoes = validate_data['atracoes']
        del validate_data['atracoes']

        endereco = validate_data['endereco']
        del validate_data['endereco']

        ponto = PontoTuristico.objects.create(**validate_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        ponto.save()
        return ponto


    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
