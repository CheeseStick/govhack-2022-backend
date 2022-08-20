from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.


class Levels(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    def get_object(self):
        return {"hello": "world"}