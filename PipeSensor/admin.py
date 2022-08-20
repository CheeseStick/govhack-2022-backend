from django.contrib import admin

from .models import PipeSensorReport


@admin.register(PipeSensorReport)
class PipeSensorReport(admin.ModelAdmin):
    list_display = ("pipe", "reported_at", "flow_rate", "water_level", )
    list_filter = ("reported_at", )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
