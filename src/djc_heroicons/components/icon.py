from typing import Any, Dict, Literal, Optional

from django_components import Component, types

from djc_heroicons.icons import IconName, ICONS


# TODO - Add once validation in django-components is fixed
#
# class IconKwargs(TypedDict):
#     name: IconName
#     variant: NotRequired[Literal["outline", "solid"]]
#     size: NotRequired[int]
#     color: NotRequired[str]
#     stroke_width: NotRequired[float]
#     viewbox: NotRequired[str]
#     attrs: NotRequired[Optional[Dict]]
# IconType = Component[EmptyTuple, IconKwargs, EmptyDict, Any, Any, Any]


class Icon(Component):
    """The icon component"""

    template: types.django_html = """
        <svg {% html_attrs attrs default_attrs %}>
            {% for path_attrs in icon_paths %}
                <path {% html_attrs path_attrs %} />
            {% endfor %}
        </svg>
    """

    def get_context_data(
        self,
        /,
        *,
        name: IconName,
        variant: Literal["outline", "solid"] = "outline",
        size: int = 24,
        color: str = "currentColor",
        stroke_width: float = 1.5,
        viewbox: str = "0 0 24 24",
        attrs: Optional[Dict] = None,
    ) -> Dict:
        if variant not in ["outline", "solid"]:
            raise ValueError(f"Invalid variant: {variant}. Must be either 'outline' or 'solid'.")

        icon_paths = ICONS.get(variant + "_" + name)

        # These are set as "default" attributes, so users can override them
        # by passing them in the `attrs` argument.
        default_attrs: Dict[str, Any] = {
            "viewBox": viewbox,
            "style": f"width: {size}px; height: {size}px",
            "aria-hidden": "true",
        }

        # The SVG applies the color differently in "outline" and "solid" versions
        if variant == "outline":
            default_attrs["fill"] = "none"
            default_attrs["stroke"] = color
            default_attrs["stroke-width"] = stroke_width
        else:
            default_attrs["fill"] = color
            default_attrs["stroke"] = "none"

        return {
            "icon_paths": icon_paths,
            "default_attrs": default_attrs,
            "attrs": attrs,
        }
