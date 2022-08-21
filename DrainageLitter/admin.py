from django.contrib import admin

from .models import Drainage


@admin.register(Drainage)
class DrainageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start_latitude", "start_longitude", "end_latitude", "end_longitude", "width", )
