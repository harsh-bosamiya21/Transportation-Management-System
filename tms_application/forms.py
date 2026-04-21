from django import forms
from .models import User
from .models import  NewCustomer, NewDriver, NewShipment
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'is_driver', 'is_customer')




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)



class CustomerForm(forms.ModelForm):
    class Meta:
        model = NewCustomer
        fields = ['customer_name', 'address', 'phone_number', 'email']  # Modify based on your model fields

class DriverForm(forms.ModelForm):
    class Meta:
        model = NewDriver
        fields = ['driver_name', 'license_number', 'phone_number', 'email', 'vehicle_type', 'vehicle_registration_number', 'vehicle_number_plate', 'available']  # Modify based on your model

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = NewShipment
        exclude = ['tracking_id']

class TrackingForm(forms.Form):
    tracking_id = forms.UUIDField(
         
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your tracking code. e.g. 987733733-GT'}),
    )

