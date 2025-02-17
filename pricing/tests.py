from django.test import TestCase
from .logic import PricingLogic
from .models import Pricing

# Create your tests here.


class PricingLogicTests(TestCase):
    
    def setUp(self):
        # Create a default pricing configuration for tests purpose
        Pricing.objects.create(
            base_fare=2.5,
            per_km_rate=1.0,
            traffic_multiplier_high=1.5,
            demand_multiplier_peak=1.8,
        )
    # Base fare + (Distance fare * 1) = Distance fare => Total * traffic = Total fare

    def test_standard_fare_calculation(self):
        result = PricingLogic.calculate_fare(5, 'low', 'normal')
        self.assertEqual(result['total_fare'], 7.5)
    
    def test_high_traffic_pricing(self):
        result = PricingLogic.calculate_fare(8, 'high', 'normal')
        self.assertEqual(result['total_fare'], 15.75)

    def test_surge_pricing_high_demand(self):
        result = PricingLogic.calculate_fare(12, 'normal', 'peak')
        self.assertEqual(result['total_fare'], 26.1)
        
        
    def test_peak_hour_with_high_traffic(self):
        result = PricingLogic.calculate_fare(7, 'high', 'peak')
        self.assertEqual(result['total_fare'], 25.65)

    def test_long_distance_ride(self):
        result = PricingLogic.calculate_fare(20, 'low', 'normal')
        self.assertEqual(result['total_fare'], 22.5)