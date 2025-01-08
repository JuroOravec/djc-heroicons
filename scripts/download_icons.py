from contextlib import contextmanager
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, NamedTuple

from playwright.sync_api import sync_playwright


@contextmanager
def playwright_context():
    """
    Context manager to create and close Playwright browser instance.

    ```python
    with playwright_context() as browser:
        page = browser.new_page()
        page.goto("https://example.com")
    ```
    """
    # Setup
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
    )

    yield browser

    # Teardown
    browser.close()
    playwright.stop()


class IconGroup(NamedTuple):
    group: str
    icons: List[Dict]


def download_icons():
    all_names = set()
    icon_groups: List[IconGroup] = []

    with playwright_context() as browser:
        page = browser.new_page()
        page.goto("https://www.heroicons.com/")

        # First download the icons
        for variant in ["outline", "solid"]:
            page.locator(f"button:has-text('{variant.capitalize()}')").click()
            page.wait_for_timeout(1000)

            data = page.eval_on_selector_all(
                '[role="tabpanel"] .group',
                """
                (els) => {
                    const data = els.map((el) => {
                        const paths = [...el.querySelectorAll('svg path')].map((p) => {
                            return p.getAttributeNames().reduce((acc, key) => {
                                acc[key] = p.getAttribute(key);
                                return acc;
                            }, {});
                        });
                        const name = el.textContent.trim();
                        return {
                            name,
                            paths,
                        };
                    });
                    return data;
                }
                """,
            )
            icon_groups.append(IconGroup(variant, data))

    # Once all icons are downloaded, write them to a file
    content = "ICONS: Dict[VariantName, Dict[IconName, List[Dict[str, str]]]] = {}\n"
    for group in icon_groups:
        content += f"\n# {group.group.capitalize()}\n" f'ICONS["{group.group}"] = {{}}\n'
        for item in group.icons:
            name = item["name"]
            paths = item["paths"]
            all_names.add(name)
            content += f'ICONS["{group.group}"]["{name}"] = {paths}\n'

    icon_name_literals = sorted([f'"{name}"' for name in all_names])
    icon_type = 'VariantName = Literal["outline", "solid"]'
    icon_type += f'\n    IconName = Literal[{", ".join(icon_name_literals)}]'

    content = (
        dedent(
            f"""
    # fmt: off
    '''
    This file defines SVG PATHS of material design icons.

    Don't use these icons directly. Instead, use the the `icon` component
    defined in `components/icon.py`.

    The icon definitions were taken from Heroicons.com - Free-to-use (MIT license) iconset from
    the makers of Tailwind CSS.

    The icons were extracted from the website using `scripts/download_icons.py`.
    '''

    from typing import Dict, List, Literal

    {icon_type}

    """
        )
        + content
    )

    return content


def main():
    icons_script = download_icons()
    Path("src/djc_heroicons/icons.py").write_text(icons_script)


if __name__ == "__main__":
    main()
