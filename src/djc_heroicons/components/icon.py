import difflib
from typing import Any, Dict, NamedTuple, Optional

from django.template import Context
from django_components import Component, Empty, types

from djc_heroicons.icons import ICONS, IconName, VariantName


class Icon(Component):
    """The icon component"""

    Args = Empty
    Slots = Empty

    class Kwargs(NamedTuple):
        name: IconName
        variant: VariantName
        size: int
        color: str
        stroke_width: float
        viewbox: str
        attrs: Optional[Dict]

    class Defaults:
        variant: VariantName = "outline"
        size: int = 24
        color: str = "currentColor"
        stroke_width: float = 1.5
        viewbox: str = "0 0 24 24"
        attrs: Optional[Dict] = None

    def get_template_data(self, args: Empty, kwargs: Kwargs, slots: Empty, context: Context) -> Dict:
        if kwargs.variant not in ["outline", "solid"]:
            raise ValueError(f"Invalid variant: {kwargs.variant}. Must be either 'outline' or 'solid'")

        variant_icons = ICONS[kwargs.variant]
        if kwargs.name not in variant_icons:
            # Give users a helpful message by fuzzy-search the closest key
            msg = ""
            icon_names = list(variant_icons.keys())
            if icon_names:
                fuzzy_matches = difflib.get_close_matches(kwargs.name, icon_names, n=3, cutoff=0.7)
                if fuzzy_matches:
                    suggestions = ", ".join([f"'{match}'" for match in fuzzy_matches])
                    msg += f". Did you mean any of {suggestions}?"

            raise ValueError(f"Invalid icon name: {kwargs.name}{msg}")

        icon_paths = variant_icons[kwargs.name]

        # These are set as "default" attributes, so users can override them
        # by passing them in the `attrs` argument.
        default_attrs: Dict[str, Any] = {
            "viewBox": kwargs.viewbox,
            "style": f"width: {kwargs.size}px; height: {kwargs.size}px",
            "aria-hidden": "true",
        }

        # The SVG applies the color differently in "outline" and "solid" versions
        if kwargs.variant == "outline":
            default_attrs["fill"] = "none"
            default_attrs["stroke"] = kwargs.color
            default_attrs["stroke-width"] = kwargs.stroke_width
        else:
            default_attrs["fill"] = kwargs.color
            default_attrs["stroke"] = "none"

        return {
            "icon_paths": icon_paths,
            "default_attrs": default_attrs,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}
        <svg {% html_attrs attrs default_attrs %}>
            {% for path_attrs in icon_paths %}
                <path {% html_attrs path_attrs %} />
            {% endfor %}
        </svg>
    """
