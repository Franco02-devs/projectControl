from apps.records.models import Location

from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Location
        exclude = ('state','created_date', 'modified_date', 'deleted_date')
        