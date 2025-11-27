from playwright.sync_api import Page, expect
from pytest_playwright_axe import Axe

from pages.login_page import LoginPage

def test_login_page_accessibility(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()

    axe = Axe()

    results = axe.run(page)

    violations = results["violations"]

    violations_count = len(violations)

    if violations_count > 0:
        print(f"{violations_count} accessibility violations was found:")
        for violation in violations:
            print(f"- {violation['id']}: {violation['help']}")

    assert violations_count == 0, f"{violations_count} accessibility violations was found!"