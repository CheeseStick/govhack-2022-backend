from django.urls import path
from .views.lists import PipeList

app_name = "pipe_network"

urlpatterns = [
    path("", PipeList.as_view(), name="pipe_list")
]
