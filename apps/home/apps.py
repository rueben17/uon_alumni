# apps.py
from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.home'  # or whatever your app name is

    def ready(self):
        import apps.home.signals  # Register signals