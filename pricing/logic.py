from .models import Pricing

class PricingLogic:
    
    @staticmethod
    def get_pricing_config():
        # Get the latest pricing configuration from the database
        # If no configuration exists, create a default one
        config, created = Pricing.objects.get_or_create(id=1)
        return config

    @staticmethod
    def calculate_fare(distance, traffic_level, demand_level):
       
        config = PricingLogic.get_pricing_config()

        # Calculate base fare and distance fare
        distance_fare = distance * config.per_km_rate
        total_fare = config.base_fare + distance_fare

        # Apply traffic multiplier
        if traffic_level == 'high':
            total_fare *= config.traffic_multiplier_high
        elif traffic_level == 'normal':
            pass  

        # Apply demand multiplier
        if demand_level == 'peak':
            total_fare *= config.demand_multiplier_peak
        elif demand_level == 'normal':
            pass  

        return {
            "base_fare": config.base_fare,
            "distance_fare": distance_fare,
            "traffic_multiplier": config.traffic_multiplier_high if traffic_level == 'high' else 1.0,
            "demand_multiplier": config.demand_multiplier_peak if demand_level == 'peak' else 1.0,
            "total_fare": round(total_fare, 2),
        }