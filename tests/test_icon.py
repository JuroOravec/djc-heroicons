import pytest
from django.template import Context, Library, Template
from django_components import Component, ComponentRegistry, NotRegistered, types

from .testutils import BaseTestCase


class TestIcon(BaseTestCase):
    def test_icon(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon"
                name='ellipsis-vertical'
                color="red"
                attrs:class="self-center cursor-pointer"
            / %}
        """
        rendered: str = Template(template_str).render(Context())

        assert rendered.strip() == (
            "<!-- _RENDERED Icon_0d23cf,a1bc3f,, -->\n"
            '<svg aria-hidden="true" class="self-center cursor-pointer" data-djc-id-a1bc3f fill="none" stroke="red" stroke-width="1.5" style="width: 24px; height: 24px" viewbox="0 0 24 24">\n'
            '<path d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" stroke-linecap="round" stroke-linejoin="round"></path>\n'
            "</svg>"
        )  # noqa: E501

    def test_icon_with_variant(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon"
                name='ellipsis-vertical'
                variant="solid"
                color="red"
                attrs:class="self-center cursor-pointer"
            / %}
        """
        rendered: str = Template(template_str).render(Context())

        assert rendered.strip() == (
            "<!-- _RENDERED Icon_0d23cf,a1bc3f,, -->\n"
            '<svg aria-hidden="true" class="self-center cursor-pointer" data-djc-id-a1bc3f fill="red" stroke="none" style="width: 24px; height: 24px" viewbox="0 0 24 24">\n'
            '<path clip-rule="evenodd" d="M10.5 6a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm0 6a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm0 6a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Z" fill-rule="evenodd"></path>\n'
            "</svg>"
        )  # noqa: E501

    def test_icon_with_invalid_variant(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon"
                name='ellipsis-vertical'
                variant="invalid_variant"
            / %}
        """

        with pytest.raises(ValueError, match="Invalid variant: invalid_variant. Must be either 'outline' or 'solid'"):
            Template(template_str).render(Context())

    def test_gives_helpful_message_on_invalid_name(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon"
                name='ellipsis-invalid'
                color="red"
                attrs:class="self-center cursor-pointer"
            / %}
        """

        with pytest.raises(
            ValueError,
            match="Invalid icon name: ellipsis-invalid. Did you mean any of 'ellipsis-horizontal', 'ellipsis-vertical'?"
        ):
            Template(template_str).render(Context())

    def test_icon_with_custom_attributes(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon"
                name='ellipsis-vertical'
                attrs:class="custom-class"
                attrs:data-test="test"
            / %}
        """
        rendered: str = Template(template_str).render(Context())

        assert rendered.strip() == (
            "<!-- _RENDERED Icon_0d23cf,a1bc3f,, -->\n"
            '<svg aria-hidden="true" class="custom-class" data-djc-id-a1bc3f data-test="test" fill="none" stroke="currentColor" stroke-width="1.5" style="width: 24px; height: 24px" viewbox="0 0 24 24">\n'
            '<path d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" stroke-linecap="round" stroke-linejoin="round"></path>\n'
            '</svg>'
        )

    def test_icon_with_invalid_icon_name(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon"
                name='ellipsis-invalid'
            / %}
        """
        with pytest.raises(ValueError, match="Invalid icon name: ellipsis-invalid"):
            Template(template_str).render(Context())

class TestCustomIconName(BaseTestCase):
    SETTINGS_HEROICONS = {"component_name": "my_icon"}

    def test_icon_with_custom_component_name(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "my_icon"
                name='ellipsis-vertical'
                color="teal"
            / %}
        """
        rendered: str = Template(template_str).render(Context())

        assert rendered.strip() == (
            "<!-- _RENDERED Icon_0d23cf,a1bc3f,, -->\n"
            '<svg aria-hidden="true" data-djc-id-a1bc3f fill="none" stroke="teal" stroke-width="1.5" style="width: 24px; height: 24px" viewbox="0 0 24 24">\n'
            '<path d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" stroke-linecap="round" stroke-linejoin="round"></path>\n'
            "</svg>"
        )

lib = Library()
custom_registry = ComponentRegistry(library=lib)

class TestCustomIconRegistry(BaseTestCase):
    SETTINGS_HEROICONS = {"registry": custom_registry}

    def test_icon_with_custom_registry(self):
        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon" name='ellipsis-vertical' color="green" / %}
        """

        with pytest.raises(NotRegistered, match='The component "icon" is not registered'):
            Template(template_str).render(Context())

        assert issubclass(custom_registry.get("icon"), Component)
