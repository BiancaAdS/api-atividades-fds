from rest_framework import serializers
from atividades import models

class AtividadesEtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AtividadesEtapa
        fields = '__all__'

class SubAtividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubAtividades
        fields = '__all__'

class EtapasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Etapa
        fields = '__all__'