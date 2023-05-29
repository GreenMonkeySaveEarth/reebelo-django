from django.contrib import admin

# Register your models here.
from quickstart.models import InventoryModel, TrackingModel, OrderModel

admin.site.register(InventoryModel)
admin.site.register(TrackingModel)
admin.site.register(OrderModel)