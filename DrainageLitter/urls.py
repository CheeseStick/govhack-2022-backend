from django.urls import path

from .views.drainage_list import GetDrainagesListAPI
from .views.litters_list import LittersListInDrainagesAPI

app_name = "drainage_litter"


urlpatterns = [
    path("", GetDrainagesListAPI.as_view()),
    path("litter/", LittersListInDrainagesAPI.as_view()),
]
