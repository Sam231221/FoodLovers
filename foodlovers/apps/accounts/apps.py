from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foodlovers.apps.accounts'

    def ready(self):
        import foodlovers.apps.accounts.signals
