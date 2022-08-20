from PipeNetwork.models import Pipe
from PipeNetwork.serializers import PipeWithGeometrySerializer
from rest_framework import generics, exceptions
from rest_framework.permissions import AllowAny


class PipeList(generics.ListAPIView):
    serializer_class = PipeWithGeometrySerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        start_lat = self.request.query_params.get('start_lat', 0)
        end_lat = self.request.query_params.get('end_lat', 0)
        start_long = self.request.query_params.get('start_long', 0)
        end_long = self.request.query_params.get('end_long', 0)

        try:
            start_lat = float(start_lat)
            end_lat = float(end_lat)
            start_long = float(start_long)
            end_long = float(end_long)

        except ValueError:
            raise exceptions.ParseError(detail="Bad coordinates!")

        else:
            queryset = Pipe.objects.filter(geometries__latitude__range=(start_lat,end_lat),
                                           geometries__longitude__range=(start_long,end_long)).distinct()

            if queryset.count() > 1000:
                raise exceptions.NotAcceptable(detail="Server returns too many pipes!")

            return queryset
