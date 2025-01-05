from django.test import SimpleTestCase
from django_components.component_registry import registry


class BaseTestCase(SimpleTestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
        registry.clear()
