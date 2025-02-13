from django.urls import path
from pricing.views import CalculateFareView


app_name = 'pricing'

urlpatterns = [
    path('api/calculate-fare/', CalculateFareView.as_view(), name='calculate-fare'),
]