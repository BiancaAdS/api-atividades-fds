from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from atividades.api import serializers
from atividades import models

from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser


@parser_classes([FormParser]) 
class AtividadesEtapaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadesEtapaSerializer
    queryset = models.AtividadesEtapa.objects.all()
    
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['criado_em', 'sequencia']
    filterset_fields = ['etapaPertencente']

@parser_classes([FormParser]) 
class EtapasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EtapasSerializer
    queryset = models.Etapa.objects.all()
    
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['sequencia']
    filterset_fields = ['sequencia']