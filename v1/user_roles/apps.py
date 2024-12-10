from django.apps import AppConfig


class UserRolesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'v1.user_roles'

    def ready(self):
        import v1.user_roles.signals_user_roles
