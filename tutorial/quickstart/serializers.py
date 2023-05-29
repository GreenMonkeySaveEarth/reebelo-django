from rest_framework import serializers
from .models import InventoryModel, TrackingModel, OrderModel

class OrderSeriializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('id', 'tracking', 'product', 'status', 'address')
        
    def create(self, validated_data):
        tracking = TrackingModel.objects.create()
        print('validated_data = ', validated_data)
        order = OrderModel.objects.create(tracking=tracking, **validated_data)
        
        return order

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = ('id', 'name', 'quantity', 'price')
        
class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingModel
        fields = ('id', 'tracking_number', 'tracking_company')
        