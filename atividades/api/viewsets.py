from rest_framework import viewsets, filters
from atividades.api import serializers
from atividades import models

from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser


@parser_classes([FormParser]) 
class AtividadesEtapaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadesEtapaSerializer
    queryset = models.AtividadesEtapa.objects.all()
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['criado_em', 'sequencia']

@parser_classes([FormParser]) 
class EtapasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EtapasSerializer
    queryset = models.Etapa.objects.all()
    
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['sequencia']