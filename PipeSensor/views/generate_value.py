from rest_framework import views, permissions, exceptions, response, status

from django.conf import settings

from GovHack2022.math_utility import gen_wave


class GenerateSensorValueAPI(views.APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, *args, **kwargs):
        if hasattr(settings, "NOISE_PROFILES"):
            noise_profiles = getattr(settings, "NOISE_PROFILES")

            try:
                start_idx = int(self.request.query_params.get("start_idx", 0))
                end_idx = int(self.request.query_params.get("end_idx", 0))
                seed = float(self.request.query_params.get("seed", 0.0))
                noise_profile_idx = int(self.request.query_params.get("noise_profile_idx", 0))

                if not(0 <= noise_profile_idx < 10):
                    raise IndexError(f"Index overflow! Expected value between 0 and 10 but received {noise_profile_idx}")

            except ValueError as e:
                print(f"Failed to parse - {e}")
                raise exceptions.ParseError(detail="Failed to parse required query params.")

            except IndexError as e:
                print(f"Noise profile index overflow - {e}")
                raise exceptions.ParseError(detail="Bad noise profile index.")

            else:
                profile = noise_profiles[noise_profile_idx]
                wave = gen_wave.generate_wave(seed)
                final_wave = profile + wave
                generated_val = final_wave[start_idx:end_idx]

                return response.Response(data={"values": generated_val},
                                         status=status.HTTP_200_OK)

        else:
            raise exceptions.APIException(detail="Noise profile is not initialised.", code=504)
