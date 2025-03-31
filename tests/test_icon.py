import pytest
from django.template import Context, Library, Template
from django_components import Component, ComponentRegistry, NotRegistered, registry as djc_registry, types
from django_components.testing import djc_test

from djc_heroicons.apps import register_icon_component

from .testutils import setup_test_config


setup_test_config()


lib = Library()
custom_registry = ComponentRegistry(library=lib)


@djc_test
class TestIcon:
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
            "        \n"
            '        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="red" stroke-width="1.5" class="self-center cursor-pointer" style="width: 24px; height: 24px;" data-djc-id-a1bc3f="">\n'
            "            \n"
            '                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />\n'
            "            \n"
            "        </svg>"
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
            "        \n"
            '        <svg viewBox="0 0 24 24" aria-hidden="true" fill="red" stroke="none" class="self-center cursor-pointer" style="width: 24px; height: 24px;" data-djc-id-a1bc3f="">\n'
            "            \n"
            '                <path fill-rule="evenodd" d="M10.5 6a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm0 6a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Zm0 6a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0Z" clip-rule="evenodd" />\n'
            "            \n"
            "        </svg>"
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
            match="Invalid icon name: ellipsis-invalid. Did you mean any of 'ellipsis-horizontal', 'ellipsis-vertical'?",
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
            "        \n"
            '        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" data-test="test" class="custom-class" style="width: 24px; height: 24px;" data-djc-id-a1bc3f="">\n'
            "            \n"
            '                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />\n'
            "            \n"
            "        </svg>"
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

    @djc_test(django_settings={"DJC_HEROICONS": {"component_name": "my_icon"}})
    def test_icon_with_custom_component_name(self):
        # Re-register the component under the correct name
        if djc_registry.has("icon"):
            djc_registry.unregister("icon")
        register_icon_component()

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
            "        \n"
            '        <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="teal" stroke-width="1.5" style="width: 24px; height: 24px;" data-djc-id-a1bc3f="">\n'
            "            \n"
            '                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 12.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5ZM12 18.75a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5Z" />\n'
            "            \n"
            "        </svg>"
        )

    @djc_test(django_settings={"DJC_HEROICONS": {"registry": custom_registry}})
    def test_icon_with_custom_registry(self):
        # Re-register the component under the correct registry
        if djc_registry.has("icon"):
            djc_registry.unregister("icon")
        register_icon_component()

        template_str: types.django_html = """
            {% load component_tags %}
            {% component "icon" name='ellipsis-vertical' color="green" / %}
        """

        with pytest.raises(NotRegistered, match='The component "icon" is not registered'):
            Template(template_str).render(Context())

        assert issubclass(custom_registry.get("icon"), Component)
