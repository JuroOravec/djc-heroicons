from django.http import HttpResponse
from django_components import Component, types

from djc_heroicons.icons import ICONS


# Generates a page with all icons
class IconsPage(Component):
    template: types.django_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>djc-heroicons</title>
        </head>
        <body>
        {% for group_name, icons in icon_groups.items %}
            <h2>{{ group_name }}</h2>
            <div class="icons-grid">
            {% for icon_name in icons %}
                <div class="icon">
                    {% component "icon" name=icon_name variant=group_name size=256 / %}
                    <code>{{ group_name }}_{{ icon_name }}</code>
                </div>
            {% endfor %}
            </div>
        {% endfor %}
        </body>
        </html>
    """

    css: types.css = """
        .icons-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            font-size: 12px;
        }
        .icon {
            flex: 1 0 250px;
            display: flex;
            width: fit-content;
            flex-direction: column;
            align-items: center;
            gap: 16px;
            padding-top: 8px;
            padding-bottom: 8px;
        }
        """

    def get_context_data(self) -> dict:
        icon_groups: dict = {}
        for key, val in ICONS.items():
            prefix, name = key.split("_", maxsplit=1)
            if prefix not in icon_groups:
                icon_groups[prefix] = []
            icon_groups[prefix].append(name)

        return {
            "icon_groups": icon_groups,
        }

    def get(self, request, /) -> HttpResponse:
        return self.render_to_response()
