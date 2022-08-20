from django.shortcuts import render
from PipeNetwork.models import Pipe
from PipeNetwork.serializers import PipeWithGeometrySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
# Create your views here.


class PipeList(generics.ListAPIView):
    queryset = Pipe.objects.all()
    serializer_class = PipeWithGeometrySerializer
    permission_classes = [AllowAny]

