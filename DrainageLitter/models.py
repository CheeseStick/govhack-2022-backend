from django.db import models


class Drainage(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, unique=True, null=False, db_index=True)
    name = models.CharField(max_length=128)

    start_latitude = models.DecimalField(default=0.0, decimal_places=16, max_digits=24)
    start_longitude = models.DecimalField(default=0.0, decimal_places=16, max_digits=24)

    end_latitude = models.DecimalField(default=0.0, decimal_places=16, max_digits=24)
    end_longitude = models.DecimalField(default=0.0, decimal_places=16, max_digits=24)

    width = models.FloatField(default=0.0)

    above_high_tide = models.IntegerField(default=0)
    below_high_tide = models.IntegerField(default=0)

    def __str__(self):
        return f"({self.id}) {self.name}"
