from rest_framework.routers import DefaultRouter
from apps.records.api.views.record_viewsets import RecordViewSet
from apps.records.api.views.general_views import *

router=DefaultRouter()

router.register(r'records', RecordViewSet, basename='records')
router.register(r'locations', LocationViewset, basename='locations')

urlpatterns= router.urls