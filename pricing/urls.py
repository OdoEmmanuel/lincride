from django.urls import path
from pricing.views import CalculateFareView


app_name = 'api'

urlpatterns = [
    path('calculate-fare/', CalculateFareView.as_view(), name='calculate-fare'),
]