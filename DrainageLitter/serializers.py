from rest_framework import serializers

from DrainageLitter.models import Drainage


class DrainageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drainage
        fields = '__all__'
