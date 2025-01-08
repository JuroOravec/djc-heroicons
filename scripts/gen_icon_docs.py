import subprocess
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from textwrap import dedent
from typing import Dict, List, NamedTuple

import requests
from playwright.sync_api import sync_playwright


SERVER_PORT = "8000"
SERVER_URL = f"http://127.0.0.1:{SERVER_PORT}"


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


@contextmanager
def django_dev_server_context():
    """
    Context manager to run Django development server in the background.

    ```python
    with django_dev_server_context():
        # Run tests that require Django server
        pass
    ```
    """
    # Get the path where testserver is defined, so the command doesn't depend
    # on user's current working directory.
    server_dir = (Path(__file__).parent.parent / "demo").resolve()

    # Start the Django dev server in the background
    print("Starting Django dev server...")
    proc = subprocess.Popen(
        # NOTE: Use `sys.executable` so this works both for Unix and Windows OS
        [sys.executable, "manage.py", "runserver", f"127.0.0.1:{SERVER_PORT}", "--noreload"],
        cwd=server_dir,
    )

    # Wait for the server to start by polling
    start_time = time.time()
    while time.time() - start_time < 30:  # timeout after 30 seconds
        try:
            response = requests.get(SERVER_URL)
            if response.status_code == 200:
                print("Django dev server is up and running.")
                break
        except requests.RequestException:
            time.sleep(0.1)
    else:
        proc.terminate()
        raise RuntimeError("Django server failed to start within the timeout period")

    yield  # Hand control back to the test session

    # Teardown: Kill the server process after the tests
    proc.terminate()
    proc.wait()

    print("Django dev server stopped.")


def gen_icon_images():
    # Remove any old images
    Path("assets").mkdir(exist_ok=True)
    for file in Path("assets").rglob("*.png"):
        file.unlink()

    # Open the icons page and take screenshots of each icon
    with django_dev_server_context():
        with playwright_context() as browser:
            page = browser.new_page()
            page.goto(SERVER_URL)

            icon_el = page.locator(".icon")
            icons_count = icon_el.count()
            for index in range(icons_count):
                nth_icon = icon_el.nth(index)
                icon_name = nth_icon.locator("code").text_content()
                nth_icon.locator("svg").screenshot(path=f"assets/{icon_name}.png", scale="css")


class IconData(NamedTuple):
    name: str
    group: str
    path: Path


def gen_icons_readme():
    ASSETS_DIR = "assets"
    # Read all files from the assets directory
    # and insert them into the template below
    icon_files = sorted(Path(ASSETS_DIR).rglob("*.png"))

    icon_groups: Dict[str, List[IconData]] = {}
    for file in icon_files:
        prefix, name = file.stem.split("_", maxsplit=1)
        if prefix not in icon_groups:
            icon_groups[prefix] = []
        icon_groups[prefix].append(IconData(name, prefix, file))

    icons_html = "## Icons\n\n"

    icon_grid_css = "display: flex; " "flex-wrap: wrap; " "font-family: monospace; "
    icon_css = (
        "flex: 1 0 auto; "
        "display: flex; "
        "width: 240px; "
        "flex-direction: column; "
        "align-items: center; "
        "gap: 8px; "
        "padding-top: 8px; "
        "padding-bottom: 8px; "
    )

    for group_name, group_icons in icon_groups.items():
        icons_html += f"\n\n---\n\n### {group_name.capitalize()}\n\n"

        group_html = f'<div style="{icon_grid_css}">'
        for icon in group_icons:
            group_html += dedent(
                f"""
                <div style="{icon_css}">
                    <img src="https://raw.githubusercontent.com/JuroOravec/djc-heroicons/main/{ASSETS_DIR}/{icon.path.name}" width="50">
                    {icon.name}
                </div>
                """  # noqa: E501
            )
        group_html += "</div>\n"
        icons_html += group_html

    return icons_html


# README contains markers where the grid of all icons should be inserted.
# This function reads the README, inserts the icons grid, and writes it back
def update_readme(new_content: str):
    readme = Path("README.md")
    readme_content = readme.read_text()
    start_marker = "<!-- INSERT_ICONS_START -->"
    end_marker = "<!-- INSERT_ICONS_END -->"

    # These indices are set such that, when we insert the new content, the markers REMAIN.
    # Thus we can run the script multiple times.
    start_index = readme_content.index(start_marker) + len(start_marker)
    end_index = readme_content.index(end_marker)

    new_readme_content = readme_content[:start_index] + "\n" + new_content + "\n" + readme_content[end_index:]

    readme.write_text(new_readme_content)


def main():
    gen_icon_images()
    icons_html = gen_icons_readme()
    update_readme(icons_html)


if __name__ == "__main__":
    main()
