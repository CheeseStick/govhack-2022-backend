from PipeNetwork.models import Pipe
from PipeNetwork.serializers import PipeWithGeometryAndFlowRateSerializer

from rest_framework import generics, exceptions, permissions


class PipeListByGeometryAPI(generics.ListAPIView):
    serializer_class = PipeWithGeometryAndFlowRateSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        try:
            coord_1_lat = float(self.request.query_params.get("lat_p1", 0.0))
            coord_1_lon = float(self.request.query_params.get("lon_p1", 0.0))
            coord_2_lat = float(self.request.query_params.get("lat_p2", 0.0))
            coord_2_lon = float(self.request.query_params.get("lon_p2", 0.0))

            latitudes = (coord_1_lat, coord_2_lat) if coord_1_lat < coord_2_lat else (coord_2_lat, coord_1_lat)
            longitudes = (coord_1_lon, coord_2_lon) if coord_1_lon < coord_2_lon else (coord_2_lon, coord_1_lon)

        except ValueError:
            raise exceptions.ParseError(detail="Bad query!")

        else:
            queryset = Pipe.objects.filter(geometries__latitude__gte=latitudes[0], geometries__latitude__lte=latitudes[1],
                                           geometries__longitude__gte=longitudes[0], geometries__longitude__lte=longitudes[1]).distinct()

            # print(queryset)
            # print(queryset.count())

            if 4096 < queryset.count():
                raise exceptions.NotAcceptable(detail=f"Server returns too many pipes - Server returned {queryset.count()}")

            return queryset
