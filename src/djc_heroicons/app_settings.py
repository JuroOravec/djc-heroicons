from importlib import import_module
from typing import NamedTuple, Optional, Union

from django.conf import settings
from django_components import ComponentRegistry


class HeroIconsSettings(NamedTuple):
    """
    Settings available for djc_heroicons.

    **Example:**

    ```python
    custom_registry = ComponentRegistry()

    DJC_HEROICONS = HeroIconsSettings(
        registry=custom_registry,
    )
    ```
    """

    registry: Optional[Union[ComponentRegistry, str]] = None
    """
    The component registry to which the icon component should be registered.

    If `None`, the icon is registered into the default registry.

    ```python
    custom_registry = ComponentRegistry()

    DJC_HEROICONS = HeroIconsSettings(
        registry=custom_registry,
    )
    ```
    """

    component_name: Optional[str] = None
    """
    The name under which the Icon component will be available from within Django templates.

    If `None`, the component is registered with the name "icon".

    That means you can use the component in your templates like this:

    ```html
    {% component "icon" name="academic-cap" / %}
    ```

    **Example:**

    If you set this to "heroicons":

    ```python
    DJC_HEROICONS = HeroIconsSettings(
        component_name="heroicons",
    )
    ```

    You will use the component like this:

    ```html
    {% component "heroicons" name="academic-cap" / %}
    ```
    """


class InternalSettings:
    @property
    def _settings(self) -> HeroIconsSettings:
        data = getattr(settings, "DJC_HEROICONS", {})
        return HeroIconsSettings(**data) if not isinstance(data, HeroIconsSettings) else data

    @property
    def REGISTRY(self) -> ComponentRegistry:
        registry_or_import = self._settings.registry
        if registry_or_import is None:
            registry_or_import = "django_components.registry"

        if isinstance(registry_or_import, str):
            module_name, attr = registry_or_import.rsplit(".", 1)
            registry = getattr(import_module(module_name), attr)
        else:
            registry = registry_or_import

        return registry

    @property
    def COMPONENT_NAME(self) -> str:
        component_name = self._settings.component_name
        if component_name is None:
            component_name = "icon"

        return component_name


app_settings = InternalSettings()
