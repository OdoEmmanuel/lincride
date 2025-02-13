from django.db import models

# Create your models here.

class Pricing(models.Model):
    base_fare = models.FloatField(default=2.5)
    per_km_rate = models.FloatField(default=1.0)
    traffic_multiplier_high = models.FloatField(default=1.5)
    demand_multiplier_peak = models.FloatField(default=1.8)

    def __str__(self):
        return f"Pricing (ID: {self.id})"