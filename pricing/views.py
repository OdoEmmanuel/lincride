from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FareCalculationSerializer
from .logic import PricingLogic

# Create your views here.

class CalculateFareView(APIView):
    def get(self, request):
        serializer = FareCalculationSerializer(data=request.query_params)
        if serializer.is_valid():
            distance = serializer.validated_data['distance']
            traffic_level = serializer.validated_data['traffic_level']
            demand_level = serializer.validated_data['demand_level']

            fare_details = PricingLogic.calculate_fare(distance, traffic_level, demand_level)
            return Response(fare_details, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)