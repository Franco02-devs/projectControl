from apps.base.api import GeneralListApiView
from apps.records.api.serializers.record_serializers import RecordSerializer

class RecordListApiView(GeneralListApiView):
    serializer_class= RecordSerializer
