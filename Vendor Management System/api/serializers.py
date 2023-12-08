from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from django.core.validators import MinValueValidator,MaxValueValidator

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {
            'on_time_delivery_rate': {'validators': [MinValueValidator(0), MaxValueValidator(100)]},
            'quality_rating_avg': {'validators': [MinValueValidator(0), MaxValueValidator(5)]},
            'average_response_time': {'validators': [MinValueValidator(0)]},
            'fulfillment_rate': {'validators': [MinValueValidator(0), MaxValueValidator(100)]},
        }

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_kwargs = {
            'quantity': {'validators': [MinValueValidator(1)]},
            'quality_rating': {'validators': [MinValueValidator(0), MaxValueValidator(5)]},
        }

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
        extra_kwargs = {
            'on_time_delivery_rate': {'validators': [MinValueValidator(0), MaxValueValidator(100)]},
            'quality_rating_avg': {'validators': [MinValueValidator(0), MaxValueValidator(5)]},
            'average_response_time': {'validators': [MinValueValidator(0)]},
            'fulfillment_rate': {'validators': [MinValueValidator(0), MaxValueValidator(100)]},
        }
