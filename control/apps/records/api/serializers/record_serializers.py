from apps.records.models import Record
from rest_framework import serializers

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        exclude = ('state','created_date', 'modified_date', 'deleted_date')