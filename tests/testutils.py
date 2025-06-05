from pathlib import Path
from typing import Dict, Optional

import django
from django.conf import settings


def setup_test_config(heroicons: Optional[Dict] = None):
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
            "autodiscover": False,
        },
        "DJC_HEROICONS": {
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

    settings.configure(**default_settings)
    django.setup()
