from django.apps import AppConfig


class MadUserConfig(AppConfig):
    name = 'mad_user'

    def ready(self):
        import mad_user.signals