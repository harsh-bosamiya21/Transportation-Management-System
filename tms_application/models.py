from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField('Is customer', default=False)
    is_driver = models.BooleanField('Is driver', default=False)

# Customer Model
class NewCustomer(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.customer_name


# Driver Model
from django.db import models

class NewDriver(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('ST', 'Small Truck'),
        ('FT', 'Flatbed Truck'),
        ('TrR', 'Trailer Truck'),
        ('TkT', 'Tanker Truck'),
        ('CT', 'Container Truck'),
        ('MV', 'Mini Van'),
    ]
    
    AVAILABLE_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    
    driver_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    vehicle_type = models.CharField(max_length=3, choices=VEHICLE_TYPE_CHOICES)
    vehicle_registration_number = models.CharField(max_length=50)
    vehicle_number_plate = models.CharField(max_length=20)
    available = models.BooleanField(choices=AVAILABLE_CHOICES)

    def __str__(self):
        return self.driver_name



# Shipment Model
class NewShipment(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    DESTINATION_CHOICES = [
        ('MI', 'Mumbai'),
        ('DL', 'Delhi'),
        ('AMD', 'Ahmedabad'),
    ]

    customer = models.ForeignKey(NewCustomer, on_delete=models.CASCADE, blank=True, null=True, default="default")
    order_date = models.DateField(blank=True, null=True)
    shipment_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    package_description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    driver = models.ForeignKey(NewDriver, on_delete=models.SET_NULL, null=True, blank=True, default="default")
    from_destination = models.CharField(max_length=255, choices=DESTINATION_CHOICES, default='MI')
    to_destination = models.CharField(max_length=255, choices=DESTINATION_CHOICES, default='DL')

    def __str__(self):
        if self.customer:
            return f"Shipment {self.tracking_id} for {self.customer.customer_name}"
        else:
            return f"Shipment {self.tracking_id} (No customer assigned)"
        


class Package(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    receiver_email = models.EmailField()
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.receiver_name}"

