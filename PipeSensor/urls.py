from django.urls import path
from .views.levels import Levels

app_name = "pipe_sensor"

urlpatterns = [
    path("", Levels.as_view())
]
