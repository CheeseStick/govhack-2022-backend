from rest_framework import serializers

from PipeSensor.models import PipeSensorReport


class PipeSensorReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = PipeSensorReport
        fields = '__all__'
