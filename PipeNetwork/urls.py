from django.urls import path

from .views.pipe_list_by_geometry import PipeListByGeometryAPI
from .views.pipe_list import PipeListAPI

app_name = "pipe_network"

urlpatterns = [
    path("", PipeListByGeometryAPI.as_view(), name="pipe_list_by_geometry"),
    path("all/", PipeListAPI.as_view(), name="pipe_list"),
]
