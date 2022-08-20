from rest_framework import serializers
from .models import Pipe, PipeGeometry

class PipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipe
        fields = '__all__'


class PipeGeometrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PipeGeometry
        fields = '__all__'


class PipeWithGeometrySerializer(serializers.ModelSerializer):
    geometries = PipeGeometrySerializer(many=True, read_only=True)

    class Meta:
        model = Pipe
        fields = '__all__'
