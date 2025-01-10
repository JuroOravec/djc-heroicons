import difflib
from dataclasses import dataclass, MISSING
from typing import Any, Dict, Optional, Tuple, Type

from django_components import Component, types

from djc_heroicons.icons import ICONS, IconName, VariantName

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


# TODO - This should live in django-components
class ComponentDefaultsMeta(type):
    def __new__(mcs, name: str, bases: Tuple, namespace: Dict) -> Type:
        # Apply dataclass decorator to the class
        return dataclass(super().__new__(mcs, name, bases, namespace))


class ComponentDefaults(metaclass=ComponentDefaultsMeta):
    def __post_init__(self) -> None:
        fields = self.__class__.__dataclass_fields__  # type: ignore[attr-defined]
        for field_name, field in fields.items():
            if field.default is not MISSING:
                if getattr(self, field_name) is None:
                    setattr(self, field_name, field.default)


class IconDefaults(ComponentDefaults):
    name: IconName
    variant: VariantName = "outline"
    size: int = 24
    color: str = "currentColor"
    stroke_width: float = 1.5
    viewbox: str = "0 0 24 24"
    attrs: Optional[Dict] = None


class Icon(Component):
    """The icon component"""

    template: types.django_html = """
        {% load component_tags %}
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
        variant: Optional[VariantName] = None,
        size: Optional[int] = None,
        color: Optional[str] = None,
        stroke_width: Optional[float] = None,
        viewbox: Optional[str] = None,
        attrs: Optional[Dict] = None,
    ) -> Dict:
        kwargs = IconDefaults(**self.input.kwargs)

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
