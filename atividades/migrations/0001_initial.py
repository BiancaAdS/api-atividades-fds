# Generated by Django 4.1 on 2022-11-09 00:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadesEtapa1',
            fields=[
                ('id_atv', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('titleAtv', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=60)),
                ('descr', models.CharField(max_length=1500)),
                ('link', models.CharField(blank=True, default='', max_length=500)),
                ('descrLink', models.CharField(blank=True, default='', max_length=500)),
                ('descrTemp', models.CharField(max_length=500)),
                ('tempo', models.IntegerField()),
                ('macro', models.CharField(max_length=60)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AtividadesEtapa2',
            fields=[
                ('id_atv', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('titleAtv', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=60)),
                ('descr', models.CharField(max_length=1500)),
                ('link', models.CharField(blank=True, default='', max_length=500)),
                ('descrLink', models.CharField(blank=True, default='', max_length=500)),
                ('descrTemp', models.CharField(max_length=500)),
                ('tempo', models.IntegerField()),
                ('macro', models.CharField(max_length=60)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AtividadesEtapa3',
            fields=[
                ('id_atv', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('titleAtv', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=60)),
                ('descr', models.CharField(max_length=1500)),
                ('link', models.CharField(blank=True, default='', max_length=500)),
                ('descrLink', models.CharField(blank=True, default='', max_length=500)),
                ('descrTemp', models.CharField(max_length=500)),
                ('tempo', models.IntegerField()),
                ('macro', models.CharField(max_length=60)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AtividadesEtapa4',
            fields=[
                ('id_atv', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('titleAtv', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=60)),
                ('descr', models.CharField(max_length=1500)),
                ('link', models.CharField(blank=True, default='', max_length=500)),
                ('descrLink', models.CharField(blank=True, default='', max_length=500)),
                ('descrTemp', models.CharField(max_length=500)),
                ('tempo', models.IntegerField()),
                ('macro', models.CharField(max_length=60)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
