from django.urls import path
from apps.records.api.views.general_views import LocationViewset

urlpatterns = [
    path('location/', LocationViewset.as_view(), name="location"),
]
