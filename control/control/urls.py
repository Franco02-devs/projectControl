from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import Login

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de API",
      default_version='v1',
      description="Documentación pública de API de Serivicio de Gestión de Organización AQP25",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="francocahuasoto@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/',include('apps.users.api.urls')),
    path('records/', include('apps.records.api.routers')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    path('', Login.as_view(), name='Login'),
]
