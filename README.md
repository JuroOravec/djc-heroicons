# djc-heroicons

[![PyPI - Version](https://img.shields.io/pypi/v/djc-heroicons)](https://pypi.org/project/djc-heroicons/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/djc-heroicons)](https://pypi.org/project/djc-heroicons/) [![PyPI - License](https://img.shields.io/pypi/l/djc-heroicons)](https://github.com/JuroOravec/djc-heroicons/blob/main/LICENSE) [![PyPI - Downloads](https://img.shields.io/pypi/dm/djc-heroicons)](https://pypistats.org/packages/djc-heroicons) [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/JuroOravec/djc-heroicons/tests.yml)](https://github.com/JuroOravec/djc-heroicons/actions/workflows/tests.yml)

_[HeroIcons.com](https://heroicons.com) icons for django-components._

## Overview

djc-heroicons adds an `Icon` component that renders an `<svg>` element with the icons from [HeroIcons.com](https://heroicons.com). This icon is accessible in Django templates as `{% component "icon" %}`.

Use the `name` kwarg to specify the icon name:

```django
<div>
  Items:
  <ul>
    <li>
      {% component "icon" name="academic-cap" / %}
    </li>
  </ul>
</div>
```

By default the component renders the `"outline"` variant. To render the `"solid"` variant of the icon, set kwarg `variant` to `"solid"`:

```django
{% component "icon" name="academic-cap" variant="solid" / %}
```

Common changes like color, size, or stroke width can all be set directly on the component:

```django
{% component "icon"
   name="academic-cap"
   size=48
   color="red"
   stroke_width=1.2
/ %}
```

If you need to pass attributes to the `<svg>` element, you can use the `attrs` kwarg, which accepts a dictionary:

```django
{% component "icon"
   name="academic-cap"
   attrs:id="my-svg"
   attrs:class="p-4 mb-3"
   attrs:data-id="test-123"
/ %}
```

See all available input for `Icon` component in [API reference](#api-reference).

## Usage in Python

All of the above is possible also from within Python, by importing `Icon`:

```py
from djc_heroicons import Icon

content = Icon.render(
    kwargs={
        "name": "academic-cap",
        "variant": "solid",
        "size": 48,
        "attrs": {
            "id": "my-svg",
            "class": "p-4 mb-3",
        },
    },
)
```

## Settings

You can configure the behavior of the djc-heroicons library
by setting a `HEROICONS` variable in your Django settings file.

`HEROICONS` can be either a plain dictionary, or a instance of `HeroIconSettings`. The latter helps with intellisense and type hints:

```py
HEROICONS = {
   "registry": custom_registry,
}

# or

from djc_heroicons import HeroIconsSettings

HEROICONS = HeroIconsSettings(
   registry=custom_registry,
)
```

### `registry`

`ComponentRegistry | str | None = None`

The django-components' [`ComponentRegistry`](https://emilstenstrom.github.io/django-components/latest/concepts/advanced/component_registry/) to which the icon component should be registered.

If `None`, the icon is registered into the default registry.

```python
custom_registry = ComponentRegistry()

HEROICONS = HeroIconsSettings(
   registry=custom_registry,
)
```

### `component_name`

`str | None = "icon"`

The name under which the Icon component will be available from within Django templates.

If `None`, the component is registered with the name `"icon"`.

```html
{% component "icon" name="academic-cap" / %}
```

**Example:**

If you set this to `"heroicons"`:

```python
HEROICONS = HeroIconsSettings(
   component_name="heroicons",
)
```

You will use the component like this:

```html
{% component "heroicons" name="academic-cap" / %}
```

## API reference

### `Icon` / `{% component "icon" %}`

The Icon component accepts following kwargs:

#### `name`

`str` - required

The icon name from [HeroIcons.com](https://heroicons.com), e.g. `arrow-left-circle`.

#### `variant`

`"outline" | "solid" = "outline"`

The icon variant - `"outline"` or `"solid"`. Defaults to `"outline"`.

#### `size`

`int = 24`

The icon size in pixels. Defaults to `24`.

#### `color`

`str = "currentColor"`

The icon color. Defaults to `"currentColor"`.

- If the icon is `"outline"`, this sets the stroke color.
- If the icon is `"solid"`, this sets the fill color.

#### `stroke_width`

`float = 1.5`

The icon [stroke width](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/stroke-width). Applies only to the `"outline"` variant. Defaults to `1.5`.

#### `viewbox`

`str = "0 0 24 24"`

The icon SVG's [viewbox](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/viewbox). Defaults to `"0 0 24 24"`.

#### `attrs`

`Dict | None = None`

Optional dictionary to pass HTML attributes to the icon's SVG element.

### `HeroIconsSettings`

NamedTuple for adding intellisense and type hinting to the settings. See [Settings](#settings).

### `IconName`

Type alias that holds all the valid icon names, e.g.

`Literal["arrow-left-circle", "arrow-down", ...]`

Use this for type validation and intellisense.

**Example:**

In the example below, the `"icon"` key of `menu` is typed, so Mypy or other linters pick it up as an error:

```py
from typing import List, TypedDict

from djc_heroicons import IconName

class MenuItem(TypedDict):
    name: str
    icon: IconName

menu: List[MenuItem]: = [
   {"name": "Home", "icon": "home"},
   {"name": "Settings", "icon": "cog-6-tooth"},
   {"name": "Account", "icon": "user-circe"},  <-- Typo!
]
```

## Release notes

Read the [Release Notes](https://github.com/JuroOravec/djc-heroicons/tree/main/CHANGELOG.md)
to see the latest features and fixes.

<!-- INSERT_ICONS_START -->
## Icons



---

### Outline

<div style="display: flex; flex-wrap: wrap; font-family: monospace; ">
<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_academic-cap.png" width="50">
    academic-cap
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_adjustments-horizontal.png" width="50">
    adjustments-horizontal
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_adjustments-vertical.png" width="50">
    adjustments-vertical
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_archive-box-arrow-down.png" width="50">
    archive-box-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_archive-box-x-mark.png" width="50">
    archive-box-x-mark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_archive-box.png" width="50">
    archive-box
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down-circle.png" width="50">
    arrow-down-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down-left.png" width="50">
    arrow-down-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down-on-square-stack.png" width="50">
    arrow-down-on-square-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down-on-square.png" width="50">
    arrow-down-on-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down-right.png" width="50">
    arrow-down-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down-tray.png" width="50">
    arrow-down-tray
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-down.png" width="50">
    arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-left-circle.png" width="50">
    arrow-left-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-left-end-on-rectangle.png" width="50">
    arrow-left-end-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-left-start-on-rectangle.png" width="50">
    arrow-left-start-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-left.png" width="50">
    arrow-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-long-down.png" width="50">
    arrow-long-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-long-left.png" width="50">
    arrow-long-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-long-right.png" width="50">
    arrow-long-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-long-up.png" width="50">
    arrow-long-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-path-rounded-square.png" width="50">
    arrow-path-rounded-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-path.png" width="50">
    arrow-path
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-right-circle.png" width="50">
    arrow-right-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-right-end-on-rectangle.png" width="50">
    arrow-right-end-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-right-start-on-rectangle.png" width="50">
    arrow-right-start-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-right.png" width="50">
    arrow-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-top-right-on-square.png" width="50">
    arrow-top-right-on-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-trending-down.png" width="50">
    arrow-trending-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-trending-up.png" width="50">
    arrow-trending-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-down-left.png" width="50">
    arrow-turn-down-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-down-right.png" width="50">
    arrow-turn-down-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-left-down.png" width="50">
    arrow-turn-left-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-left-up.png" width="50">
    arrow-turn-left-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-right-down.png" width="50">
    arrow-turn-right-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-right-up.png" width="50">
    arrow-turn-right-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-up-left.png" width="50">
    arrow-turn-up-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-turn-up-right.png" width="50">
    arrow-turn-up-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up-circle.png" width="50">
    arrow-up-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up-left.png" width="50">
    arrow-up-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up-on-square-stack.png" width="50">
    arrow-up-on-square-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up-on-square.png" width="50">
    arrow-up-on-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up-right.png" width="50">
    arrow-up-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up-tray.png" width="50">
    arrow-up-tray
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-up.png" width="50">
    arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-uturn-down.png" width="50">
    arrow-uturn-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-uturn-left.png" width="50">
    arrow-uturn-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-uturn-right.png" width="50">
    arrow-uturn-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrow-uturn-up.png" width="50">
    arrow-uturn-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrows-pointing-in.png" width="50">
    arrows-pointing-in
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrows-pointing-out.png" width="50">
    arrows-pointing-out
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrows-right-left.png" width="50">
    arrows-right-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_arrows-up-down.png" width="50">
    arrows-up-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_at-symbol.png" width="50">
    at-symbol
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_backspace.png" width="50">
    backspace
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_backward.png" width="50">
    backward
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_banknotes.png" width="50">
    banknotes
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-2.png" width="50">
    bars-2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-3-bottom-left.png" width="50">
    bars-3-bottom-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-3-bottom-right.png" width="50">
    bars-3-bottom-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-3-center-left.png" width="50">
    bars-3-center-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-3.png" width="50">
    bars-3
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-4.png" width="50">
    bars-4
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-arrow-down.png" width="50">
    bars-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bars-arrow-up.png" width="50">
    bars-arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_battery-0.png" width="50">
    battery-0
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_battery-100.png" width="50">
    battery-100
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_battery-50.png" width="50">
    battery-50
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_beaker.png" width="50">
    beaker
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bell-alert.png" width="50">
    bell-alert
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bell-slash.png" width="50">
    bell-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bell-snooze.png" width="50">
    bell-snooze
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bell.png" width="50">
    bell
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bold.png" width="50">
    bold
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bolt-slash.png" width="50">
    bolt-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bolt.png" width="50">
    bolt
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_book-open.png" width="50">
    book-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bookmark-slash.png" width="50">
    bookmark-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bookmark-square.png" width="50">
    bookmark-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bookmark.png" width="50">
    bookmark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_briefcase.png" width="50">
    briefcase
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_bug-ant.png" width="50">
    bug-ant
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_building-library.png" width="50">
    building-library
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_building-office-2.png" width="50">
    building-office-2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_building-office.png" width="50">
    building-office
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_building-storefront.png" width="50">
    building-storefront
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cake.png" width="50">
    cake
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_calculator.png" width="50">
    calculator
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_calendar-date-range.png" width="50">
    calendar-date-range
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_calendar-days.png" width="50">
    calendar-days
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_calendar.png" width="50">
    calendar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_camera.png" width="50">
    camera
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chart-bar-square.png" width="50">
    chart-bar-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chart-bar.png" width="50">
    chart-bar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chart-pie.png" width="50">
    chart-pie
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-bottom-center-text.png" width="50">
    chat-bubble-bottom-center-text
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-bottom-center.png" width="50">
    chat-bubble-bottom-center
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-left-ellipsis.png" width="50">
    chat-bubble-left-ellipsis
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-left-right.png" width="50">
    chat-bubble-left-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-left.png" width="50">
    chat-bubble-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-oval-left-ellipsis.png" width="50">
    chat-bubble-oval-left-ellipsis
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chat-bubble-oval-left.png" width="50">
    chat-bubble-oval-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_check-badge.png" width="50">
    check-badge
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_check-circle.png" width="50">
    check-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_check.png" width="50">
    check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-double-down.png" width="50">
    chevron-double-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-double-left.png" width="50">
    chevron-double-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-double-right.png" width="50">
    chevron-double-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-double-up.png" width="50">
    chevron-double-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-down.png" width="50">
    chevron-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-left.png" width="50">
    chevron-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-right.png" width="50">
    chevron-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-up-down.png" width="50">
    chevron-up-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_chevron-up.png" width="50">
    chevron-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_circle-stack.png" width="50">
    circle-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_clipboard-document-check.png" width="50">
    clipboard-document-check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_clipboard-document-list.png" width="50">
    clipboard-document-list
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_clipboard-document.png" width="50">
    clipboard-document
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_clipboard.png" width="50">
    clipboard
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_clock.png" width="50">
    clock
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cloud-arrow-down.png" width="50">
    cloud-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cloud-arrow-up.png" width="50">
    cloud-arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cloud.png" width="50">
    cloud
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_code-bracket-square.png" width="50">
    code-bracket-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_code-bracket.png" width="50">
    code-bracket
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cog-6-tooth.png" width="50">
    cog-6-tooth
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cog-8-tooth.png" width="50">
    cog-8-tooth
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cog.png" width="50">
    cog
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_command-line.png" width="50">
    command-line
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_computer-desktop.png" width="50">
    computer-desktop
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cpu-chip.png" width="50">
    cpu-chip
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_credit-card.png" width="50">
    credit-card
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cube-transparent.png" width="50">
    cube-transparent
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cube.png" width="50">
    cube
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_currency-bangladeshi.png" width="50">
    currency-bangladeshi
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_currency-dollar.png" width="50">
    currency-dollar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_currency-euro.png" width="50">
    currency-euro
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_currency-pound.png" width="50">
    currency-pound
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_currency-rupee.png" width="50">
    currency-rupee
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_currency-yen.png" width="50">
    currency-yen
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cursor-arrow-rays.png" width="50">
    cursor-arrow-rays
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_cursor-arrow-ripple.png" width="50">
    cursor-arrow-ripple
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_device-phone-mobile.png" width="50">
    device-phone-mobile
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_device-tablet.png" width="50">
    device-tablet
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_divide.png" width="50">
    divide
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-arrow-down.png" width="50">
    document-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-arrow-up.png" width="50">
    document-arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-chart-bar.png" width="50">
    document-chart-bar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-check.png" width="50">
    document-check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-currency-bangladeshi.png" width="50">
    document-currency-bangladeshi
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-currency-dollar.png" width="50">
    document-currency-dollar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-currency-euro.png" width="50">
    document-currency-euro
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-currency-pound.png" width="50">
    document-currency-pound
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-currency-rupee.png" width="50">
    document-currency-rupee
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-currency-yen.png" width="50">
    document-currency-yen
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-duplicate.png" width="50">
    document-duplicate
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-magnifying-glass.png" width="50">
    document-magnifying-glass
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-minus.png" width="50">
    document-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-plus.png" width="50">
    document-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document-text.png" width="50">
    document-text
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_document.png" width="50">
    document
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_ellipsis-horizontal-circle.png" width="50">
    ellipsis-horizontal-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_ellipsis-horizontal.png" width="50">
    ellipsis-horizontal
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_ellipsis-vertical.png" width="50">
    ellipsis-vertical
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_envelope-open.png" width="50">
    envelope-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_envelope.png" width="50">
    envelope
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_equals.png" width="50">
    equals
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_exclamation-circle.png" width="50">
    exclamation-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_exclamation-triangle.png" width="50">
    exclamation-triangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_eye-dropper.png" width="50">
    eye-dropper
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_eye-slash.png" width="50">
    eye-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_eye.png" width="50">
    eye
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_face-frown.png" width="50">
    face-frown
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_face-smile.png" width="50">
    face-smile
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_film.png" width="50">
    film
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_finger-print.png" width="50">
    finger-print
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_fire.png" width="50">
    fire
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_flag.png" width="50">
    flag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_folder-arrow-down.png" width="50">
    folder-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_folder-minus.png" width="50">
    folder-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_folder-open.png" width="50">
    folder-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_folder-plus.png" width="50">
    folder-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_folder.png" width="50">
    folder
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_forward.png" width="50">
    forward
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_funnel.png" width="50">
    funnel
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_gif.png" width="50">
    gif
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_gift-top.png" width="50">
    gift-top
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_gift.png" width="50">
    gift
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_globe-alt.png" width="50">
    globe-alt
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_globe-americas.png" width="50">
    globe-americas
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_globe-asia-australia.png" width="50">
    globe-asia-australia
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_globe-europe-africa.png" width="50">
    globe-europe-africa
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_h1.png" width="50">
    h1
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_h2.png" width="50">
    h2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_h3.png" width="50">
    h3
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_hand-raised.png" width="50">
    hand-raised
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_hand-thumb-down.png" width="50">
    hand-thumb-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_hand-thumb-up.png" width="50">
    hand-thumb-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_hashtag.png" width="50">
    hashtag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_heart.png" width="50">
    heart
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_home-modern.png" width="50">
    home-modern
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_home.png" width="50">
    home
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_identification.png" width="50">
    identification
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_inbox-arrow-down.png" width="50">
    inbox-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_inbox-stack.png" width="50">
    inbox-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_inbox.png" width="50">
    inbox
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_information-circle.png" width="50">
    information-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_italic.png" width="50">
    italic
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_key.png" width="50">
    key
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_language.png" width="50">
    language
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_lifebuoy.png" width="50">
    lifebuoy
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_light-bulb.png" width="50">
    light-bulb
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_link-slash.png" width="50">
    link-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_link.png" width="50">
    link
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_list-bullet.png" width="50">
    list-bullet
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_lock-closed.png" width="50">
    lock-closed
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_lock-open.png" width="50">
    lock-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_magnifying-glass-circle.png" width="50">
    magnifying-glass-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_magnifying-glass-minus.png" width="50">
    magnifying-glass-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_magnifying-glass-plus.png" width="50">
    magnifying-glass-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_magnifying-glass.png" width="50">
    magnifying-glass
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_map-pin.png" width="50">
    map-pin
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_map.png" width="50">
    map
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_megaphone.png" width="50">
    megaphone
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_microphone.png" width="50">
    microphone
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_minus-circle.png" width="50">
    minus-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_minus.png" width="50">
    minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_moon.png" width="50">
    moon
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_musical-note.png" width="50">
    musical-note
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_newspaper.png" width="50">
    newspaper
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_no-symbol.png" width="50">
    no-symbol
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_numbered-list.png" width="50">
    numbered-list
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_paint-brush.png" width="50">
    paint-brush
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_paper-airplane.png" width="50">
    paper-airplane
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_paper-clip.png" width="50">
    paper-clip
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_pause-circle.png" width="50">
    pause-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_pause.png" width="50">
    pause
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_pencil-square.png" width="50">
    pencil-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_pencil.png" width="50">
    pencil
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_percent-badge.png" width="50">
    percent-badge
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_phone-arrow-down-left.png" width="50">
    phone-arrow-down-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_phone-arrow-up-right.png" width="50">
    phone-arrow-up-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_phone-x-mark.png" width="50">
    phone-x-mark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_phone.png" width="50">
    phone
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_photo.png" width="50">
    photo
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_play-circle.png" width="50">
    play-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_play-pause.png" width="50">
    play-pause
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_play.png" width="50">
    play
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_plus-circle.png" width="50">
    plus-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_plus.png" width="50">
    plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_power.png" width="50">
    power
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_presentation-chart-bar.png" width="50">
    presentation-chart-bar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_presentation-chart-line.png" width="50">
    presentation-chart-line
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_printer.png" width="50">
    printer
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_puzzle-piece.png" width="50">
    puzzle-piece
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_qr-code.png" width="50">
    qr-code
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_question-mark-circle.png" width="50">
    question-mark-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_queue-list.png" width="50">
    queue-list
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_radio.png" width="50">
    radio
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_receipt-percent.png" width="50">
    receipt-percent
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_receipt-refund.png" width="50">
    receipt-refund
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_rectangle-group.png" width="50">
    rectangle-group
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_rectangle-stack.png" width="50">
    rectangle-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_rocket-launch.png" width="50">
    rocket-launch
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_rss.png" width="50">
    rss
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_scale.png" width="50">
    scale
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_scissors.png" width="50">
    scissors
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_server-stack.png" width="50">
    server-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_server.png" width="50">
    server
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_share.png" width="50">
    share
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_shield-check.png" width="50">
    shield-check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_shield-exclamation.png" width="50">
    shield-exclamation
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_shopping-bag.png" width="50">
    shopping-bag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_shopping-cart.png" width="50">
    shopping-cart
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_signal-slash.png" width="50">
    signal-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_signal.png" width="50">
    signal
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_slash.png" width="50">
    slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_sparkles.png" width="50">
    sparkles
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_speaker-wave.png" width="50">
    speaker-wave
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_speaker-x-mark.png" width="50">
    speaker-x-mark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_square-2-stack.png" width="50">
    square-2-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_square-3-stack-3d.png" width="50">
    square-3-stack-3d
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_squares-2x2.png" width="50">
    squares-2x2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_squares-plus.png" width="50">
    squares-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_star.png" width="50">
    star
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_stop-circle.png" width="50">
    stop-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_stop.png" width="50">
    stop
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_strikethrough.png" width="50">
    strikethrough
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_sun.png" width="50">
    sun
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_swatch.png" width="50">
    swatch
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_table-cells.png" width="50">
    table-cells
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_tag.png" width="50">
    tag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_ticket.png" width="50">
    ticket
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_trash.png" width="50">
    trash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_trophy.png" width="50">
    trophy
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_truck.png" width="50">
    truck
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_tv.png" width="50">
    tv
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_underline.png" width="50">
    underline
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_user-circle.png" width="50">
    user-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_user-group.png" width="50">
    user-group
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_user-minus.png" width="50">
    user-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_user-plus.png" width="50">
    user-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_user.png" width="50">
    user
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_users.png" width="50">
    users
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_variable.png" width="50">
    variable
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_video-camera-slash.png" width="50">
    video-camera-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_video-camera.png" width="50">
    video-camera
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_view-columns.png" width="50">
    view-columns
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_viewfinder-circle.png" width="50">
    viewfinder-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_wallet.png" width="50">
    wallet
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_wifi.png" width="50">
    wifi
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_window.png" width="50">
    window
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_wrench-screwdriver.png" width="50">
    wrench-screwdriver
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_wrench.png" width="50">
    wrench
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_x-circle.png" width="50">
    x-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/outline_x-mark.png" width="50">
    x-mark
</div>
</div>


---

### Solid

<div style="display: flex; flex-wrap: wrap; font-family: monospace; ">
<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_academic-cap.png" width="50">
    academic-cap
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_adjustments-horizontal.png" width="50">
    adjustments-horizontal
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_adjustments-vertical.png" width="50">
    adjustments-vertical
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_archive-box-arrow-down.png" width="50">
    archive-box-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_archive-box-x-mark.png" width="50">
    archive-box-x-mark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_archive-box.png" width="50">
    archive-box
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down-circle.png" width="50">
    arrow-down-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down-left.png" width="50">
    arrow-down-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down-on-square-stack.png" width="50">
    arrow-down-on-square-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down-on-square.png" width="50">
    arrow-down-on-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down-right.png" width="50">
    arrow-down-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down-tray.png" width="50">
    arrow-down-tray
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-down.png" width="50">
    arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-left-circle.png" width="50">
    arrow-left-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-left-end-on-rectangle.png" width="50">
    arrow-left-end-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-left-start-on-rectangle.png" width="50">
    arrow-left-start-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-left.png" width="50">
    arrow-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-long-down.png" width="50">
    arrow-long-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-long-left.png" width="50">
    arrow-long-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-long-right.png" width="50">
    arrow-long-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-long-up.png" width="50">
    arrow-long-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-path-rounded-square.png" width="50">
    arrow-path-rounded-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-path.png" width="50">
    arrow-path
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-right-circle.png" width="50">
    arrow-right-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-right-end-on-rectangle.png" width="50">
    arrow-right-end-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-right-start-on-rectangle.png" width="50">
    arrow-right-start-on-rectangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-right.png" width="50">
    arrow-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-top-right-on-square.png" width="50">
    arrow-top-right-on-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-trending-down.png" width="50">
    arrow-trending-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-trending-up.png" width="50">
    arrow-trending-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-down-left.png" width="50">
    arrow-turn-down-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-down-right.png" width="50">
    arrow-turn-down-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-left-down.png" width="50">
    arrow-turn-left-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-left-up.png" width="50">
    arrow-turn-left-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-right-down.png" width="50">
    arrow-turn-right-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-right-up.png" width="50">
    arrow-turn-right-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-up-left.png" width="50">
    arrow-turn-up-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-turn-up-right.png" width="50">
    arrow-turn-up-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up-circle.png" width="50">
    arrow-up-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up-left.png" width="50">
    arrow-up-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up-on-square-stack.png" width="50">
    arrow-up-on-square-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up-on-square.png" width="50">
    arrow-up-on-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up-right.png" width="50">
    arrow-up-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up-tray.png" width="50">
    arrow-up-tray
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-up.png" width="50">
    arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-uturn-down.png" width="50">
    arrow-uturn-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-uturn-left.png" width="50">
    arrow-uturn-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-uturn-right.png" width="50">
    arrow-uturn-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrow-uturn-up.png" width="50">
    arrow-uturn-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrows-pointing-in.png" width="50">
    arrows-pointing-in
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrows-pointing-out.png" width="50">
    arrows-pointing-out
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrows-right-left.png" width="50">
    arrows-right-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_arrows-up-down.png" width="50">
    arrows-up-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_at-symbol.png" width="50">
    at-symbol
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_backspace.png" width="50">
    backspace
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_backward.png" width="50">
    backward
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_banknotes.png" width="50">
    banknotes
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-2.png" width="50">
    bars-2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-3-bottom-left.png" width="50">
    bars-3-bottom-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-3-bottom-right.png" width="50">
    bars-3-bottom-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-3-center-left.png" width="50">
    bars-3-center-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-3.png" width="50">
    bars-3
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-4.png" width="50">
    bars-4
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-arrow-down.png" width="50">
    bars-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bars-arrow-up.png" width="50">
    bars-arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_battery-0.png" width="50">
    battery-0
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_battery-100.png" width="50">
    battery-100
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_battery-50.png" width="50">
    battery-50
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_beaker.png" width="50">
    beaker
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bell-alert.png" width="50">
    bell-alert
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bell-slash.png" width="50">
    bell-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bell-snooze.png" width="50">
    bell-snooze
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bell.png" width="50">
    bell
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bold.png" width="50">
    bold
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bolt-slash.png" width="50">
    bolt-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bolt.png" width="50">
    bolt
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_book-open.png" width="50">
    book-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bookmark-slash.png" width="50">
    bookmark-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bookmark-square.png" width="50">
    bookmark-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bookmark.png" width="50">
    bookmark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_briefcase.png" width="50">
    briefcase
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_bug-ant.png" width="50">
    bug-ant
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_building-library.png" width="50">
    building-library
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_building-office-2.png" width="50">
    building-office-2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_building-office.png" width="50">
    building-office
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_building-storefront.png" width="50">
    building-storefront
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cake.png" width="50">
    cake
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_calculator.png" width="50">
    calculator
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_calendar-date-range.png" width="50">
    calendar-date-range
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_calendar-days.png" width="50">
    calendar-days
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_calendar.png" width="50">
    calendar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_camera.png" width="50">
    camera
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chart-bar-square.png" width="50">
    chart-bar-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chart-bar.png" width="50">
    chart-bar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chart-pie.png" width="50">
    chart-pie
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-bottom-center-text.png" width="50">
    chat-bubble-bottom-center-text
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-bottom-center.png" width="50">
    chat-bubble-bottom-center
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-left-ellipsis.png" width="50">
    chat-bubble-left-ellipsis
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-left-right.png" width="50">
    chat-bubble-left-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-left.png" width="50">
    chat-bubble-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-oval-left-ellipsis.png" width="50">
    chat-bubble-oval-left-ellipsis
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chat-bubble-oval-left.png" width="50">
    chat-bubble-oval-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_check-badge.png" width="50">
    check-badge
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_check-circle.png" width="50">
    check-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_check.png" width="50">
    check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-double-down.png" width="50">
    chevron-double-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-double-left.png" width="50">
    chevron-double-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-double-right.png" width="50">
    chevron-double-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-double-up.png" width="50">
    chevron-double-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-down.png" width="50">
    chevron-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-left.png" width="50">
    chevron-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-right.png" width="50">
    chevron-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-up-down.png" width="50">
    chevron-up-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_chevron-up.png" width="50">
    chevron-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_circle-stack.png" width="50">
    circle-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_clipboard-document-check.png" width="50">
    clipboard-document-check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_clipboard-document-list.png" width="50">
    clipboard-document-list
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_clipboard-document.png" width="50">
    clipboard-document
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_clipboard.png" width="50">
    clipboard
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_clock.png" width="50">
    clock
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cloud-arrow-down.png" width="50">
    cloud-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cloud-arrow-up.png" width="50">
    cloud-arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cloud.png" width="50">
    cloud
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_code-bracket-square.png" width="50">
    code-bracket-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_code-bracket.png" width="50">
    code-bracket
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cog-6-tooth.png" width="50">
    cog-6-tooth
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cog-8-tooth.png" width="50">
    cog-8-tooth
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cog.png" width="50">
    cog
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_command-line.png" width="50">
    command-line
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_computer-desktop.png" width="50">
    computer-desktop
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cpu-chip.png" width="50">
    cpu-chip
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_credit-card.png" width="50">
    credit-card
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cube-transparent.png" width="50">
    cube-transparent
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cube.png" width="50">
    cube
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_currency-bangladeshi.png" width="50">
    currency-bangladeshi
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_currency-dollar.png" width="50">
    currency-dollar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_currency-euro.png" width="50">
    currency-euro
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_currency-pound.png" width="50">
    currency-pound
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_currency-rupee.png" width="50">
    currency-rupee
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_currency-yen.png" width="50">
    currency-yen
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cursor-arrow-rays.png" width="50">
    cursor-arrow-rays
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_cursor-arrow-ripple.png" width="50">
    cursor-arrow-ripple
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_device-phone-mobile.png" width="50">
    device-phone-mobile
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_device-tablet.png" width="50">
    device-tablet
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_divide.png" width="50">
    divide
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-arrow-down.png" width="50">
    document-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-arrow-up.png" width="50">
    document-arrow-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-chart-bar.png" width="50">
    document-chart-bar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-check.png" width="50">
    document-check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-currency-bangladeshi.png" width="50">
    document-currency-bangladeshi
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-currency-dollar.png" width="50">
    document-currency-dollar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-currency-euro.png" width="50">
    document-currency-euro
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-currency-pound.png" width="50">
    document-currency-pound
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-currency-rupee.png" width="50">
    document-currency-rupee
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-currency-yen.png" width="50">
    document-currency-yen
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-duplicate.png" width="50">
    document-duplicate
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-magnifying-glass.png" width="50">
    document-magnifying-glass
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-minus.png" width="50">
    document-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-plus.png" width="50">
    document-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document-text.png" width="50">
    document-text
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_document.png" width="50">
    document
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_ellipsis-horizontal-circle.png" width="50">
    ellipsis-horizontal-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_ellipsis-horizontal.png" width="50">
    ellipsis-horizontal
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_ellipsis-vertical.png" width="50">
    ellipsis-vertical
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_envelope-open.png" width="50">
    envelope-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_envelope.png" width="50">
    envelope
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_equals.png" width="50">
    equals
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_exclamation-circle.png" width="50">
    exclamation-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_exclamation-triangle.png" width="50">
    exclamation-triangle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_eye-dropper.png" width="50">
    eye-dropper
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_eye-slash.png" width="50">
    eye-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_eye.png" width="50">
    eye
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_face-frown.png" width="50">
    face-frown
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_face-smile.png" width="50">
    face-smile
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_film.png" width="50">
    film
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_finger-print.png" width="50">
    finger-print
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_fire.png" width="50">
    fire
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_flag.png" width="50">
    flag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_folder-arrow-down.png" width="50">
    folder-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_folder-minus.png" width="50">
    folder-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_folder-open.png" width="50">
    folder-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_folder-plus.png" width="50">
    folder-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_folder.png" width="50">
    folder
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_forward.png" width="50">
    forward
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_funnel.png" width="50">
    funnel
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_gif.png" width="50">
    gif
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_gift-top.png" width="50">
    gift-top
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_gift.png" width="50">
    gift
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_globe-alt.png" width="50">
    globe-alt
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_globe-americas.png" width="50">
    globe-americas
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_globe-asia-australia.png" width="50">
    globe-asia-australia
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_globe-europe-africa.png" width="50">
    globe-europe-africa
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_h1.png" width="50">
    h1
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_h2.png" width="50">
    h2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_h3.png" width="50">
    h3
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_hand-raised.png" width="50">
    hand-raised
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_hand-thumb-down.png" width="50">
    hand-thumb-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_hand-thumb-up.png" width="50">
    hand-thumb-up
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_hashtag.png" width="50">
    hashtag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_heart.png" width="50">
    heart
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_home-modern.png" width="50">
    home-modern
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_home.png" width="50">
    home
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_identification.png" width="50">
    identification
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_inbox-arrow-down.png" width="50">
    inbox-arrow-down
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_inbox-stack.png" width="50">
    inbox-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_inbox.png" width="50">
    inbox
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_information-circle.png" width="50">
    information-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_italic.png" width="50">
    italic
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_key.png" width="50">
    key
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_language.png" width="50">
    language
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_lifebuoy.png" width="50">
    lifebuoy
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_light-bulb.png" width="50">
    light-bulb
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_link-slash.png" width="50">
    link-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_link.png" width="50">
    link
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_list-bullet.png" width="50">
    list-bullet
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_lock-closed.png" width="50">
    lock-closed
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_lock-open.png" width="50">
    lock-open
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_magnifying-glass-circle.png" width="50">
    magnifying-glass-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_magnifying-glass-minus.png" width="50">
    magnifying-glass-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_magnifying-glass-plus.png" width="50">
    magnifying-glass-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_magnifying-glass.png" width="50">
    magnifying-glass
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_map-pin.png" width="50">
    map-pin
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_map.png" width="50">
    map
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_megaphone.png" width="50">
    megaphone
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_microphone.png" width="50">
    microphone
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_minus-circle.png" width="50">
    minus-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_minus.png" width="50">
    minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_moon.png" width="50">
    moon
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_musical-note.png" width="50">
    musical-note
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_newspaper.png" width="50">
    newspaper
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_no-symbol.png" width="50">
    no-symbol
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_numbered-list.png" width="50">
    numbered-list
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_paint-brush.png" width="50">
    paint-brush
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_paper-airplane.png" width="50">
    paper-airplane
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_paper-clip.png" width="50">
    paper-clip
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_pause-circle.png" width="50">
    pause-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_pause.png" width="50">
    pause
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_pencil-square.png" width="50">
    pencil-square
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_pencil.png" width="50">
    pencil
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_percent-badge.png" width="50">
    percent-badge
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_phone-arrow-down-left.png" width="50">
    phone-arrow-down-left
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_phone-arrow-up-right.png" width="50">
    phone-arrow-up-right
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_phone-x-mark.png" width="50">
    phone-x-mark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_phone.png" width="50">
    phone
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_photo.png" width="50">
    photo
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_play-circle.png" width="50">
    play-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_play-pause.png" width="50">
    play-pause
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_play.png" width="50">
    play
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_plus-circle.png" width="50">
    plus-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_plus.png" width="50">
    plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_power.png" width="50">
    power
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_presentation-chart-bar.png" width="50">
    presentation-chart-bar
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_presentation-chart-line.png" width="50">
    presentation-chart-line
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_printer.png" width="50">
    printer
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_puzzle-piece.png" width="50">
    puzzle-piece
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_qr-code.png" width="50">
    qr-code
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_question-mark-circle.png" width="50">
    question-mark-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_queue-list.png" width="50">
    queue-list
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_radio.png" width="50">
    radio
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_receipt-percent.png" width="50">
    receipt-percent
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_receipt-refund.png" width="50">
    receipt-refund
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_rectangle-group.png" width="50">
    rectangle-group
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_rectangle-stack.png" width="50">
    rectangle-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_rocket-launch.png" width="50">
    rocket-launch
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_rss.png" width="50">
    rss
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_scale.png" width="50">
    scale
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_scissors.png" width="50">
    scissors
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_server-stack.png" width="50">
    server-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_server.png" width="50">
    server
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_share.png" width="50">
    share
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_shield-check.png" width="50">
    shield-check
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_shield-exclamation.png" width="50">
    shield-exclamation
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_shopping-bag.png" width="50">
    shopping-bag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_shopping-cart.png" width="50">
    shopping-cart
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_signal-slash.png" width="50">
    signal-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_signal.png" width="50">
    signal
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_slash.png" width="50">
    slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_sparkles.png" width="50">
    sparkles
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_speaker-wave.png" width="50">
    speaker-wave
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_speaker-x-mark.png" width="50">
    speaker-x-mark
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_square-2-stack.png" width="50">
    square-2-stack
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_square-3-stack-3d.png" width="50">
    square-3-stack-3d
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_squares-2x2.png" width="50">
    squares-2x2
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_squares-plus.png" width="50">
    squares-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_star.png" width="50">
    star
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_stop-circle.png" width="50">
    stop-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_stop.png" width="50">
    stop
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_strikethrough.png" width="50">
    strikethrough
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_sun.png" width="50">
    sun
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_swatch.png" width="50">
    swatch
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_table-cells.png" width="50">
    table-cells
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_tag.png" width="50">
    tag
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_ticket.png" width="50">
    ticket
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_trash.png" width="50">
    trash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_trophy.png" width="50">
    trophy
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_truck.png" width="50">
    truck
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_tv.png" width="50">
    tv
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_underline.png" width="50">
    underline
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_user-circle.png" width="50">
    user-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_user-group.png" width="50">
    user-group
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_user-minus.png" width="50">
    user-minus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_user-plus.png" width="50">
    user-plus
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_user.png" width="50">
    user
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_users.png" width="50">
    users
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_variable.png" width="50">
    variable
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_video-camera-slash.png" width="50">
    video-camera-slash
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_video-camera.png" width="50">
    video-camera
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_view-columns.png" width="50">
    view-columns
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_viewfinder-circle.png" width="50">
    viewfinder-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_wallet.png" width="50">
    wallet
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_wifi.png" width="50">
    wifi
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_window.png" width="50">
    window
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_wrench-screwdriver.png" width="50">
    wrench-screwdriver
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_wrench.png" width="50">
    wrench
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_x-circle.png" width="50">
    x-circle
</div>

<div style="flex: 1 0 auto; display: flex; width: 240px; flex-direction: column; align-items: center; gap: 8px; padding-top: 8px; padding-bottom: 8px; ">
    <img src="./assets/solid_x-mark.png" width="50">
    x-mark
</div>
</div>

<!-- INSERT_ICONS_END -->


## Development

### Tests

To run tests, use:

```bash
tox
```

### Updating icons

To download the icons from HeroIcons.com, run:

```bash
python scripts/download_icons.py
```

This will save them to `src/djc_heroicons/icons.py`.

Next, to update the list of icons in the README, run:

```bash
python scripts/gen_icon_docs.py
```
