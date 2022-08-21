import random

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


class PipeWithGeometryAndFlowRateSerializer(PipeWithGeometrySerializer):
    flow_rate = serializers.SerializerMethodField(read_only=True)

    def get_flow_rate(self, instance: Pipe):
        return random.randint(0, 2)

    class Meta:
        model = Pipe
        fields = "__all__"
