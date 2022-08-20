from datetime import datetime, timezone

from django.db import models

from PipeNetwork.models import Pipe


class PipeSensorReport(models.Model):
    pipe = models.ForeignKey(Pipe, db_index=True, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_created=True)

    flow_rate = models.FloatField("Flow Rate (m^3/s)", default=0.0)
    water_level = models.FloatField("Water Level (%)", default=0.0)

    def save(self, *args, **kwargs):
        if not hasattr(self, "id") or self.id is None:
            self.reported_at = datetime.now(tz=timezone.utc)

        super(PipeSensorReport, self).save(*args, **kwargs)
