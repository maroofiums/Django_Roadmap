from django.apps import AppConfig


class MytodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mytodo'

    def ready(self):
        import mytodo.signals