from django.db import models

class Medicion(models.Model):

    sensor_data = models.FloatField("sensor_data", null=False, blank=False)
    
    class Meta:
        verbose_name_plural = "Mediciones"

    def __str__(self):
        return str(self.sensor_data)