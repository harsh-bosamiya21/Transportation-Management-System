from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import NewShipment

@receiver(post_save, sender=NewShipment)
def send_package_notification(sender, instance, created, **kwargs):
    subject = f"Update on your package with Tracking ID {instance.tracking_id}"
    if created:
        message = f"Dear {instance.customer},\n\nYour package has been created and is currently being processed.\nYour tracking ID is {instance.tracking_id}."
    else:
        message = f"Dear {instance.customer},\n\nThe status of your package with Tracking ID {instance.tracking_id} has been updated to {instance.status}."
    
    send_mail(
        subject,
        message,
        'tmsdjango@gmail.com',
        ['harshbosamiya2122005@gmail.com'],
        fail_silently=False,
    )
