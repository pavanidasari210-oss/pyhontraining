from playwright.sync_api import Playwright, sync_playwright, Page
import datetime


def test_screenshort_demo(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Partial Page screenshot (visible on the browser page)
    # page.screenshot(path=f"screenshorts/homepage.png_{timestamp}.png")  #screenshot=Name of the folder,homepage=name of the SS-image,png= SS extension

    # Full Page screenshort
    # page.screenshot(path=f"screenshorts/homepage.png_{timestamp}.png",full_page=True)

    # Particular Element Screenshort:
    # logo=page.locator(".header-logo").screenshot(path=f"screenshorts/logo.png_{timestamp}.png")

    # Specific section  of the page screenshot:
    page.locator(".product-grid.home-page-product-grid").screenshot(path=f"screenshorts/homepage.png_{timestamp}.png")


