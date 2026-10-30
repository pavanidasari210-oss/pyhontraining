import pytest
from playwright.sync_api import Playwright,sync_playwright,expect

def test_videorecording(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(
        record_video_dir="Videos/", # So by default we are in the project directory itself.# So when I do just a videos slash, this directory or folder will be created inside our project by default
        record_video_size={"width":1024,"height":768}
    )
    page=context.new_page()
    page.goto("https://www.demoblaze.com/")
    page.locator('#login2').click()
    page.locator('#loginusername').fill("Saikrishna")
    page.locator('#loginpassword').fill("Scaleio123!")
    page.get_by_role("button",name="Log in").click()
    page.wait_for_timeout(5000)
    expect(page.locator('#logout2')).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text("Welcome Saikrishna")

    context.close()
    browser.close()



