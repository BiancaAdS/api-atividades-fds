from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import routers

from atividades.api import viewsets

schema_view = get_schema_view(
   openapi.Info(
      title="Atividades FDS API",
      default_version='v1',
      description="API responsável por realizar o controle das atividades de cada etapa da aplicação Fast Design Sprint.",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

route = routers.DefaultRouter()

route.register(r'atividades/', viewsets.AtividadesEtapaViewSet, basename='AtividadesEtapa')
route.register(r'etapas/', viewsets.EtapasViewSet, basename='Etapas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
