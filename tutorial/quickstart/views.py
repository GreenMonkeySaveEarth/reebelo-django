from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import InventorySerializer, TrackingSerializer, OrderSeriializer
from quickstart.models import InventoryModel, TrackingModel, OrderModel
from rest_framework import mixins
from rest_framework import generics
from django.http import JsonResponse
from django.middleware.csrf import get_token

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = OrderModel.objects.all()
    serializer_class = OrderSeriializer
    # permission_classes = [permissions.IsAuthenticated]


class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inventory to be viewed or edited.
    """
    queryset = InventoryModel.objects.all()
    serializer_class = InventorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class TrackingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tracking to be viewed or edited.
    """
    queryset = TrackingModel.objects.all()
    serializer_class = TrackingSerializer
    # permission_classes = [permissions.IsAuthenticated]

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})