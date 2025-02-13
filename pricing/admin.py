from django.contrib import admin

# Register your models here.
from .models import Pricing

@admin.register(Pricing)
class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'base_fare', 'per_km_rate', 'traffic_multiplier_high', 'demand_multiplier_peak')