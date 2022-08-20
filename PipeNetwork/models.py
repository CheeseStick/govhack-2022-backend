from django.db import models


class Pipe(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True, null=False, db_index=True)
    asset_id = models.CharField(db_index=True, max_length=24)

    pipe_type = models.CharField(db_index=True, max_length=64, default="Unknown")
    length = models.FloatField(default=0.0)
    shape_length = models.FloatField(default=0.0)
    district = models.CharField(db_index=True, max_length=128)

    diameter = models.IntegerField(default=0)
    material = models.CharField(max_length=16, db_index=True, default="Unknown")
    depth = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class PipeGeometry(models.Model):
    pipe = models.ForeignKey(Pipe, related_name="geometries", on_delete=models.CASCADE)
    latitude = models.DecimalField(default=0.0, decimal_places=16, max_digits=24)
    longitude = models.DecimalField(default=0.0, decimal_places=16, max_digits=24)
    level = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"
