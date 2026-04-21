from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('track/', views.track, name='track'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('add_shipment/', views.add_shipment, name='add_shipment'),
   path('login/', views.user_login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]