from rest_framework import generics
from rest_framework.permissions import AllowAny
from PipeSensor.serializers import PipeSensorReportSerializer
from PipeSensor.models import PipeSensorReport

class Levels(generics.ListAPIView):
    serializer_class = PipeSensorReportSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        queryset = PipeSensorReport.objects.all()
        return queryset

