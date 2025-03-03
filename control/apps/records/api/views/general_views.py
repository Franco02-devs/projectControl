from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.records.api.serializers.general_serializers import LocationSerializer

class LocationListApiView(GeneralListApiView):
    serializer_class=LocationSerializer      
