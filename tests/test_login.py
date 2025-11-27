from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_standart_login(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(page.get_by_text("Products", exact=True)).to_be_visible()