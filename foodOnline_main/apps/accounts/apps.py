from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodOnline_main.apps.accounts'

    def ready(self):
        import foodOnline_main.apps.accounts.signals
