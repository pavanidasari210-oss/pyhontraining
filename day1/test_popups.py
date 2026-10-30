import pytest
from playwright.sync_api import sync_playwright,Playwright,Page,expect

def test_popup(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    page.locator("#PopUp").click()
    page.wait_for_timeout(5000)
    all_popups=context.pages
    print("Total no of pages:",len(all_popups))

    # Capture URL 's for all pages:
    for i in all_popups:
        print(i.url)
        title=i.title()
        if "Playwright" in title:
            i.locator("a[herf='/doc/intro']").click()
            i.wait_for_timeout(5000)
            i.close()

