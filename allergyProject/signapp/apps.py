from django.apps import AppConfig


class SignappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signapp'

    def ready(self):
        import signapp.models_bookmark