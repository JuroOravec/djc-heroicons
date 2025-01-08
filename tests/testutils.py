from pathlib import Path
from typing import Any, Dict, List, Optional
from unittest.mock import patch

import django
from django.apps import apps
from django.conf import settings
from django.utils.functional import empty

from django_components.component_registry import ComponentRegistry, all_registries


# TODO - THIS SHOULD LIVE IN DJANGO_COMPONENTS
class TestEnv:
    def __init__(self, registries: Optional[List[ComponentRegistry]] = None):
        self.registries = registries or all_registries

    def setup(self):
        self._start_gen_id_patch()

    def teardown(self):
        self._stop_gen_id_patch()

        for registry in self.registries:
            registry.clear()

        from django_components.template import template_cache

        # NOTE: There are 1-2 tests which check Templates, so we need to clear the cache
        if template_cache:
            template_cache.clear()

    # Mock the `generate` function used inside `gen_id` so it returns deterministic IDs
    def _start_gen_id_patch(self):
        # Random number so that the generated IDs are "hex-looking", e.g. a1bc3d
        self._gen_id_count = 10599485

        def mock_gen_id(*args, **kwargs):
            self._gen_id_count += 1
            return hex(self._gen_id_count)[2:]

        self._gen_id_patch = patch("django_components.util.misc.generate", side_effect=mock_gen_id)
        self._gen_id_patch.start()

    def _stop_gen_id_patch(self):
        self._gen_id_patch.stop()
        self._gen_id_count = 10599485


test_env = TestEnv()


def setup_test_config(
    components: Optional[Dict] = None,
    heroicons: Optional[Dict] = None,
    extra_settings: Optional[Dict] = None,
):
    if settings.configured:
        return

    default_settings = {
        "BASE_DIR": Path(__file__).resolve().parent,
        "INSTALLED_APPS": ("django_components", "djc_heroicons"),
        "TEMPLATES": [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
            }
        ],
        "COMPONENTS": {
            "template_cache_size": 128,
            **(components or {}),
        },
        "HEROICONS": {
            **(heroicons or {}),
        },
        "DATABASES": {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        "SECRET_KEY": "secret",
        "ROOT_URLCONF": "django_components.urls",
    }

    settings.configure(
        **{
            **default_settings,
            **(extra_settings or {}),
        }
    )


class BaseTestCase:
    SETTINGS_COMPONENTS: Dict[str, Any] = {"autodiscover": False}
    SETTINGS_HEROICONS: Dict[str, Any] = {}
    SETTINGS: Dict[str, Any] = {}

    def setup_method(self):
        # Force Django to reload the installed apps
        apps.app_configs = {}
        apps.apps_ready = False
        apps.ready = False
        apps.loading = False

        # Force Django to reload the settings
        settings._wrapped = empty

        # Setup Django with test group-specific settings
        setup_test_config(self.SETTINGS_COMPONENTS, self.SETTINGS_HEROICONS, self.SETTINGS)
        django.setup()

        # django-components setup
        test_env.setup()

    def teardown_method(self):
        test_env.teardown()
