from django.apps import AppConfig


class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'v1.carts'

    def ready(self):
        import v1.carts.signals_cart
