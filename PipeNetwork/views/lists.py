from PipeNetwork.models import Pipe
from PipeNetwork.serializers import PipeWithGeometrySerializer

from rest_framework import generics, exceptions, permissions


class PipeList(generics.ListAPIView):
    serializer_class = PipeWithGeometrySerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        try:
            coord_1_lat = self.request.query_params.get("lat_p1", 0.0)
            coord_1_lon = self.request.query_params.get("lon_p1", 0.0)
            coord_2_lat = self.request.query_params.get("lat_p2", 0.0)
            coord_2_lon = self.request.query_params.get("lon_p2", 0.0)

            latitudes = (coord_1_lat, coord_2_lat) if coord_1_lat < coord_2_lat else (coord_2_lat, coord_1_lat)
            longitudes = (coord_1_lon, coord_2_lon) if coord_1_lon < coord_2_lon else (coord_2_lon, coord_1_lon)

        except ValueError:
            raise exceptions.ParseError(detail="Bad query!")

        else:
            queryset = Pipe.objects.filter(geometries__latitude__gte=latitudes[1], geometries__latitude__lte=latitudes[0],
                                           geometries__longitude__gte=longitudes[1], geometries__longitude__lte=longitudes[0]).distinct()

            if 2048 < queryset.count():
                raise exceptions.NotAcceptable(detail=f"Server returns too many pipes - Server returned {queryset.count()}")

            return queryset
