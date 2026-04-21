from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from .forms import CustomerForm, DriverForm, ShipmentForm, TrackingForm, ContactForm, SignUpForm
from .models import NewShipment, NewCustomer, NewDriver,  Package  # Import your models
import uuid




# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    # Check if the user is a customer or a driver
    if request.user.is_customer:
        role = 'customer'
    elif request.user.is_driver:
        role = 'driver'
    else:
        role = 'guest'  # in case neither role is assigned

    print(f"User role: {role}")

    return render(request, 'home.html', {'role': role})

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f'{subject} {name}',  # Subject
                f'{message} \nFrom {email}',     # Message
                'tmsdjango@gmail.com',           # From email
                ['harshbosamiya2122005@gmail.com'], # To email
                fail_silently=False,
            )
            return render(request, 'contact.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html')

def pricing(request):
    return render(request, "pricing.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in using the renamed method
            auth_login(request, user)

            # Redirect to the home page (common for all)
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


User = get_user_model()

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Validate form inputs (you can add more validation here)
        if not username or not password:
            messages.error(request, "Username and password are required")
            return redirect('sign_up')

        # Hash the password before saving to the database
        hashed_password = make_password(password)

        # Create a new user
        user = User(username=username, password=hashed_password)

        # Set the role
        if role == 'customer':
            user.is_customer = True
        elif role == 'driver':
            user.is_driver = True

        # Save the user to the database
        user.save()

        # Redirect to login page or home page after successful registration
        messages.success(request, f"Account created successfully. Please log in.")
        return redirect('login')
    return render(request, 'sign_up.html')



# View to handle adding a customer
def add_customer(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        # Perform validation (you can customize this as needed)
        if len(phone_number) != 10:
            error = "Phone number must be 10 digits."
            return render(request, 'add_customer.html', {'error': error})
        
        # Create and save the customer object
        NewCustomer.objects.create(
            customer_name=customer_name,
            address=address,
            phone_number=phone_number,
            email=email
        )
        
        return redirect('home')  # Redirect to home or another page of your choice
    return render(request, 'add_customer.html')


# View to handle adding a driver
def add_driver(request):
    if request.method == 'POST':
        driver_name = request.POST.get('driver_name')
        license_number = request.POST.get('license_number')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        vehicle_type = request.POST.get('vehicle_type')
        vehicle_registration_number = request.POST.get('vehicle_registration_number')
        vehicle_number_plate = request.POST.get('vehicle_number_plate')
        available = request.POST.get('available') == 'true'  # Convert string 'true'/'false' to Boolean

        # Create and save the driver object
        NewDriver.objects.create(
            driver_name=driver_name,
            license_number=license_number,
            phone_number=phone_number,
            email=email,
            vehicle_type=vehicle_type,
            vehicle_registration_number=vehicle_registration_number,
            vehicle_number_plate=vehicle_number_plate,
            available=available
        )
        
        return redirect('home')  # Redirect to the home page after saving

    return render(request, 'add_driver.html')

# View to handle adding a shipment
def add_shipment(request):
    # Fetch all customers and drivers for dropdown selections
    customers = NewCustomer.objects.all()
    drivers = NewDriver.objects.all()

    # Handle form submission
    if request.method == 'POST':
        # Get the form data from the POST request
        customer_id = request.POST.get('customer')
        order_date = request.POST.get('order_date')
        shipment_date = request.POST.get('shipment_date')
        package_description = request.POST.get('package_description')
        quantity = request.POST.get('quantity')
        driver_id = request.POST.get('driver')
        from_destination = request.POST.get('from_destination')
        to_destination = request.POST.get('to_destination')
        tracking_id=uuid.uuid4()

        # Fetch customer and driver objects using their IDs
        customer = NewCustomer.objects.get(id=customer_id)
        driver = NewDriver.objects.get(id=driver_id)

        # Create a new shipment instance
        new_shipment = NewShipment(
            customer=customer,
            order_date=order_date,
            shipment_date=shipment_date,
            package_description=package_description,
            quantity=quantity,
            driver=driver,
            from_destination=from_destination,
            to_destination=to_destination,
            tracking_id=tracking_id  # Automatically generate a new tracking ID
        )

        # Save the new shipment to the database
        new_shipment.save()

        # Redirect after successful creation
        return redirect('home')  # Or redirect to another page like shipment list

    # If it's a GET request, just show the form
    return render(request, 'add_shipment.html', {
        'customers': customers,
        'drivers': drivers
    })



#Tracking 

def track(request):
    if request.method == 'POST':
        form = TrackingForm(request.POST)
        if form.is_valid():
            tracking_id = form.cleaned_data['tracking_id']
            shipment = get_object_or_404(NewShipment, tracking_id=tracking_id)
            return render(request, 'track.html', {'shipment': shipment})
    else:
        form = TrackingForm()
    return render(request, 'track.html', {'form': form})

