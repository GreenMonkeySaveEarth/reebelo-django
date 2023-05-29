from django.db import models

# Create your models here.
class InventoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.name
    
class TrackingModel(models.Model):
    id = models.AutoField(primary_key=True)
    tracking_number = models.CharField(max_length=100)
    tracking_company = models.CharField(
        max_length=100, 
        choices=[
            ('USPS', 'USPS'), 
            ('FedEx', 'FedEx'), 
            ('UPS', 'UPS'), 
        ],
        default='UPS'
    )
    
    def __str__(self) -> str:
        return self.tracking_company + self.tracking_number
    
class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    tracking = models.OneToOneField(
        TrackingModel,
        on_delete=models.CASCADE,
        blank=True,
    )
    product = models.CharField(max_length=100, default='Mac 15')
    quantity = models.IntegerField(default=1)
    status = models.CharField(
        max_length=100, 
        choices=[
            ('processing', 'processing'), 
            ('shipped', 'shipped'), 
            ('delivered', 'delivered'), 
            ('cancelled', 'cancelled')
        ],
        default='processing'
    )
    address = models.CharField(max_length=100, default='123 Main St. SF CA')
    def __str__(self) -> str:
        return str(self.id) + self.status