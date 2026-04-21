from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db.models import signals
from django.dispatch import receiver

class TmsApplicationConfig(AppConfig):
    name = 'tms_application'
    
    def ready(self):
        import tms_application.signals
