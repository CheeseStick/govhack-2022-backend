from PipeNetwork.models import Pipe
from PipeNetwork.serializers import PipeWithGeometryAndFlowRateSerializer
from PipeNetwork.paginations import PipeListPagination

from rest_framework import generics, permissions


class PipeListAPI(generics.ListAPIView):
    serializer_class = PipeWithGeometryAndFlowRateSerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = PipeListPagination
    queryset = Pipe.objects.all()
