from django.apps import AppConfig


class HeroIconsConfig(AppConfig):
    name = "djc_heroicons"

    # This is the code that gets run when user adds djc_heroicons
    # to Django's INSTALLED_APPS
    def ready(self) -> None:
        from djc_heroicons.app_settings import app_settings
        from djc_heroicons.components.icon import Icon

        # Register the component with the specified name and to the specified registry
        app_settings.REGISTRY.register(app_settings.COMPONENT_NAME, Icon)
