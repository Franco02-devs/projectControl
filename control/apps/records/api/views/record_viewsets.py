from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.records.api.serializers.record_serializers import RecordSerializer
from apps.users.authentication_mixins import Authentication

class RecordViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class= RecordSerializer
    
    def get_queryset(self, pk=None):
        if pk==None:
            return self.get_serializer().Meta.model.objects.filter(state= True)
        return self.get_serializer().Meta.model.objects.filter(state= True, id=pk).first()   
    
    def list(self, request):
        record_serializer=self.get_serializer(self.get_queryset(), many=True) 
        return Response(record_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer=self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Registro creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        record=self.get_queryset().filter(id=pk).first()
        if record:
            record.state=False
            record.save()
            return Response({'message':'Registro eliminado'},status=status.HTTP_200_OK)
        else:
            return Response({"error":"No existe un registro con esos datos"}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            record_serializer=self.serializer_class(self.get_queryset(pk), data=request.data)
            if record_serializer.is_valid():
                record_serializer.save()
                return Response(record_serializer.data, status=status.HTTP_200_OK)
            return Response(record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)