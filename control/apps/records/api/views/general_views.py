from rest_framework import generics, viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.records.api.serializers.general_serializers import LocationSerializer
from apps.records.models import Location

class LocationViewset( viewsets.GenericViewSet):
    serializer_class=LocationSerializer
    model=Location
        
    def get_queryset(self):
        return self.get_serializer().Meta().model.objects.filter(state=True)
    
    def list(self, request):
        data= self.get_queryset()
        data= self.get_serializer(data, many=True)
        return Response(data.data)
              
