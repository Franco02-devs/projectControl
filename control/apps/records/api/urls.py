from django.urls import path
from apps.records.api.views.general_views import LocationListApiView

urlpatterns = [
    path('location/', LocationListApiView.as_view(), name="location")
]
