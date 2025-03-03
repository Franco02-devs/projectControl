from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class Location(BaseModel):
    description = models.CharField('Descripción', max_length=50)
    latitude = models.FloatField('Latitud', blank=False, null=False)
    longitude = models.FloatField('Longitud', blank=False, null=False)
    historical=HistoricalRecords()   
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciónes"

    def __str__(self):
        return f"{self.latitude} - {self.longitude}"
    
class Record(BaseModel):
    time=models.TimeField()
    date=models.DateField()
    location=models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name= "")
    historical=HistoricalRecords()   
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f"{self.time} : {self.location}"





