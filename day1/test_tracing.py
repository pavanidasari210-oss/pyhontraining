import pytest
from playwright.sync_api import Playwright,sync_playwright,expect

def test_videorecording(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()

    #starting the trace
    context.tracing.start(screenshots=True,snapshots=True)

    page=context.new_page()
    page.goto("https://www.demoblaze.com/")
    page.locator('#login2').click()
    page.locator('#loginusername').fill("Saikrishna")
    page.locator('#loginpassword').fill("Scaleio123!")
    page.get_by_role("button",name="Log in").click()
    page.wait_for_timeout(5000)
    expect(page.locator('#logout2')).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text("Welcome Saikrishna")

    #stopping the trace
    context.tracing.stop(path="trace.zip")

    context.close()
    browser.close()


#Note: There are two ways to open the trace.zip file: 1. through cli command: playwright show-trace trace.zip once we execute this command, it will open trace viewer window.

# 2. playwright is provided one direct website: https://trace.playwright.dev/  here, we can directly  upload the trace.zip file to see the detailed report
