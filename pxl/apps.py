from django.apps import AppConfig


class PxlConfig(AppConfig):
    name = 'pxl'

    def ready(self):
        """Run when the app is ready."""
        from pxl import handlers
