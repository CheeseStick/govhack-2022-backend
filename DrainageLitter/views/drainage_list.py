from rest_framework import generics, exceptions, permissions

from DrainageLitter.models import Drainage
from DrainageLitter.serializers import DrainageSerializer


class GetDrainagesListAPI(generics.ListAPIView):
    serializer_class = DrainageSerializer
    permission_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        if len(self.request.query_params) == 0:
            return Drainage.objects.all()

        else:
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
                queryset = Drainage.objects.filter(start_latitude__gte=latitudes[0], start_latitude__lte=latitudes[1],
                                                   start_longitude__gte=longitudes[0], start_longitude__lte=longitudes[1]).distinct()

                # print(queryset)
                # print(queryset.count())

                if 4096 < queryset.count():
                    raise exceptions.NotAcceptable(detail=f"Server returns too many regions - Server returned {queryset.count()}")

                return queryset
