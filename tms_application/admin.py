from django.contrib import admin
from .models import User, NewCustomer, NewDriver, NewShipment, Package

# Register your models here.

# Custom User Admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_driver')
    search_fields = ('username', 'email')
    list_filter = ('is_customer', 'is_driver')

# NewCustomer Admin
class NewCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'email', 'address')
    search_fields = ('customer_name', 'email', 'phone_number')
    list_filter = ('address',)

# NewDriver Admin
class NewDriverAdmin(admin.ModelAdmin):
    list_display = (
        'driver_name', 
        'license_number', 
        'phone_number', 
        'email', 
        'vehicle_type', 
        'vehicle_registration_number', 
        'available'
    )
    search_fields = ('driver_name', 'license_number', 'phone_number', 'email')
    list_filter = ('vehicle_type', 'available')

# NewShipment Admin
class NewShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'tracking_id', 
        'customer', 
        'driver', 
        'status', 
        'shipment_date', 
        'from_destination', 
        'to_destination'
    )
    search_fields = ('tracking_id', 'customer__customer_name', 'driver__driver_name')
    list_filter = ('status', 'from_destination', 'to_destination')
    list_editable = ('status',)
    readonly_fields = ('tracking_id',)

# Package Admin
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'sender_name', 'receiver_name', 'status', 'created_at', 'updated_at')
    search_fields = ('tracking_id', 'receiver_name', 'receiver_email')
    list_filter = ('status',)
    readonly_fields = ('tracking_id', 'created_at', 'updated_at')

# Register models
admin.site.register(User, UserAdmin)
admin.site.register(NewCustomer, NewCustomerAdmin)
admin.site.register(NewDriver, NewDriverAdmin)
admin.site.register(NewShipment, NewShipmentAdmin)