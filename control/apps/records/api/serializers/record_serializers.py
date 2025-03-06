from apps.records.models import Record
from rest_framework import serializers
from apps.records.api.serializers.general_serializers import LocationSerializer

class RecordSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Record
        exclude = ('state','created_date', 'modified_date', 'deleted_date')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'location':f"{instance.location.latitude} {instance.location.longitude}" if instance.location is not None else '',
            'date':instance.date if instance.date is not None else '',            
            'time':instance.time if instance.time is not None else '',            
        }