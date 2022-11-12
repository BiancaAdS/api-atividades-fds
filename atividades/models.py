from django.db import models
from uuid import uuid4

# Create your models here.

class AtividadesEtapa(models.Model):
    id_atividade = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=500, default="", blank=True)
    tituloAtividade = models.CharField(max_length=500, default="", blank=True)
    tipo = models.CharField(max_length=60, default="", blank=True)
    descricao = models.CharField(max_length=3800, default="", blank=True)
    link = models.CharField(max_length=500, default="", blank=True)
    descricaoLink = models.CharField(max_length=500, default="", blank=True)
    descricaoTempo = models.CharField(max_length=500, default="", blank=True)
    tempoEstimado = models.IntegerField(default=0, blank=True)
    sequencia = models.IntegerField(unique=True)
    etapaPertencente = models.ForeignKey("Etapa", on_delete=models.CASCADE, related_name='etapaPertencente')
    criado_em = models.DateTimeField(auto_now_add=True)
    

class SubAtividades(models.Model):
    id_subAtividade = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    atividade = models.ForeignKey("AtividadesEtapa", on_delete=models.CASCADE, related_name='subAtividades')
    
    
class Etapa(models.Model):
    id_etada = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nomeEtapa = models.CharField(max_length=60, default="", blank=True)
    sequencia = models.IntegerField(unique=True)