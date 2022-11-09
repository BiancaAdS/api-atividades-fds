from rest_framework import serializers
from atividades import models

class AtividadesEtapa1Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtividadesEtapa1
        fields = '__all__'

class AtividadesEtapa2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtividadesEtapa2
        fields = '__all__'

class AtividadesEtapa3Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtividadesEtapa3
        fields = '__all__'
        
class AtividadesEtapa4Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtividadesEtapa4
        fields = '__all__'