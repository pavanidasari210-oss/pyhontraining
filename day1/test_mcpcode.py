import pytest
from playwright.sync_api import Page, Browser, expect


@pytest.fixture(scope="session")
def browser() -> Browser:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        try:
            b = pw.chromium.launch(headless=False, channel="chrome")
        except Exception:
            b = pw.chromium.launch(headless=False)
        yield b
        b.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    p = browser.new_page()
    yield p
    p.close()


def test_google_page_loaded_and_search_works(page: Page):
    page.goto("https://www.google.com", wait_until="domcontentloaded")

    assert "Google" in page.title()
    assert page.url.startswith("https://www.google.com")

    search_box = page.locator('textarea[name="q"]')
    assert search_box.is_visible()
    search_box.fill("Playwright Python")
    assert search_box.input_value() == "Playwright Python"

    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)

    assert "google.com" in page.url.lower()
    assert "playwright" in page.url.lower()
    expect(page.locator("body")).to_be_visible()

    page.wait_for_timeout(10000)