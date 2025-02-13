class PricingLogic:
    BASE_FARE = 2.5
    RATE_PER_KM = 1.0

    @staticmethod
    def calculate_fare(distance, traffic_level, demand_level):
        # Calculate base fare and distance fare
        distance_fare = distance * PricingLogic.RATE_PER_KM
        total_fare = PricingLogic.BASE_FARE + distance_fare

        # Apply traffic multiplier
        if traffic_level == 'high':
            total_fare *= 1.5
        elif traffic_level == 'normal':
            pass  

        # Apply demand multiplier
        if demand_level == 'peak':
            total_fare *= 1.8
        elif demand_level == 'normal':
            pass  

        return {
            "base_fare": PricingLogic.BASE_FARE,
            "distance_fare": distance_fare,
            "traffic_multiplier": 1.5 if traffic_level == 'high' else 1.0,
            "demand_multiplier": 1.8 if demand_level == 'peak' else 1.0,
            "total_fare": round(total_fare, 2),
        }