from apps.records.models import Record
from rest_framework import serializers
from apps.records.api.serializers.general_serializers import LocationSerializer

class RecordSerializer(serializers.ModelSerializer):
    location=serializers.StringRelatedField()   
    
    class Meta:
        model = Record
        exclude = ('state','created_date', 'modified_date', 'deleted_date')