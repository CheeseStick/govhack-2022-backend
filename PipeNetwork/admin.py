from django.contrib import admin
from .models import Pipe, PipeGeometry


class PipeGeometryInline(admin.TabularInline):
    model = PipeGeometry
    fields = ("latitude", "longitude", "level", )


@admin.register(Pipe)
class PipeAdmin(admin.ModelAdmin):
    fields = ("id", "asset_id", "pipe_type", "length", "district", "diameter", "material", "depth", )
    search_fields = ("id", "pipe_type", "district", "material", )
    list_filter = ("pipe_type", "district", "material", )
    inlines = (PipeGeometryInline, )
