from rest_framework import viewsets
from atividades.api import serializers
from atividades import models

from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser


@parser_classes([FormParser]) 
class AtividadesEtapa1ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadesEtapa1Serializer
    queryset = models.AtividadesEtapa1.objects.all()

    
@parser_classes([FormParser])
class AtividadesEtapa2ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadesEtapa2Serializer
    queryset = models.AtividadesEtapa2.objects.all()

@parser_classes([FormParser])
class AtividadesEtapa3ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadesEtapa3Serializer
    queryset = models.AtividadesEtapa3.objects.all()

@parser_classes([FormParser])
class AtividadesEtapa4ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadesEtapa4Serializer
    queryset = models.AtividadesEtapa4.objects.all()