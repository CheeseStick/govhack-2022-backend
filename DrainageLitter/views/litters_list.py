import requests

from rest_framework import views, exceptions, permissions, response, status

from DrainageLitter.models import Drainage
from DrainageLitter.serializers import DrainageSerializer


class LittersListInDrainagesAPI(views.APIView):
    serializer_class = DrainageSerializer
    permission_classes = [permissions.AllowAny, ]

    def get(self, *args, **kwargs):
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
            drainage_ids = [item["id"] for item in queryset.values("id")]
            litters = []
            print(drainage_ids)

            for drainage_id in drainage_ids:
                resp = requests.get(f"https://api.litterintelligence.com/api/GetSurvey?id={drainage_id}")
                litters.append(resp.json())

            return response.Response(data=litters, status=status.HTTP_200_OK)
