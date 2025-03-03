from django.urls import path
from apps.records.api.views.general_views import LocationListApiView
from apps.records.api.views.record_views import RecordListApiView

urlpatterns = [
    path('location/', LocationListApiView.as_view(), name="location"),
    path('record/', RecordListApiView.as_view(), name="record")
]
