from django.db import models
from uuid import uuid4

# Create your models here.


class AtividadesEtapa1(models.Model):
    id_atv = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=500)
    titleAtv = models.CharField(max_length=500)
    tipo = models.CharField(max_length=60)
    descr = models.CharField(max_length=1500)
    link = models.CharField(max_length=500, default="", blank=True)
    descrLink = models.CharField(max_length=500, default="", blank=True)
    descrTemp = models.CharField(max_length=500)
    tempo = models.IntegerField()
    macro = models.CharField(max_length=60)
    create_at = models.DateField(auto_now_add=True)
    
class AtividadesEtapa2(models.Model):
    id_atv = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=500)
    titleAtv = models.CharField(max_length=500)
    tipo = models.CharField(max_length=60)
    descr = models.CharField(max_length=1500)
    link = models.CharField(max_length=500, default="", blank=True)
    descrLink = models.CharField(max_length=500, default="", blank=True)
    descrTemp = models.CharField(max_length=500)
    tempo = models.IntegerField()
    macro = models.CharField(max_length=60)
    create_at = models.DateField(auto_now_add=True)

class AtividadesEtapa3(models.Model):
    id_atv = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=500)
    titleAtv = models.CharField(max_length=500)
    tipo = models.CharField(max_length=60)
    descr = models.CharField(max_length=1500)
    link = models.CharField(max_length=500, default="", blank=True)
    descrLink = models.CharField(max_length=500, default="", blank=True)
    descrTemp = models.CharField(max_length=500)
    tempo = models.IntegerField()
    macro = models.CharField(max_length=60)
    create_at = models.DateField(auto_now_add=True)
    
class AtividadesEtapa4(models.Model):
    id_atv = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=500)
    titleAtv = models.CharField(max_length=500)
    tipo = models.CharField(max_length=60)
    descr = models.CharField(max_length=1500)
    link = models.CharField(max_length=500, default="", blank=True)
    descrLink = models.CharField(max_length=500, default="", blank=True)
    descrTemp = models.CharField(max_length=500)
    tempo = models.IntegerField()
    macro = models.CharField(max_length=60)
    create_at = models.DateField(auto_now_add=True)
