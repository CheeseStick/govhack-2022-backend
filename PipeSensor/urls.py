from django.urls import path
from .views.generate_value import GenerateSensorValueAPI

app_name = "pipe_sensor"

urlpatterns = [
    path("generate/", GenerateSensorValueAPI.as_view())
]
