import pytest
from playwright.sync_api import Page,expect

def test_login(page):
    page.goto("https://www.demoblaze.com/")
    page.locator('#login2').click()
    page.locator('#loginusername').fill("Saikrishna")
    page.locator('#loginpassword').fill("Scaleio123!")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(5000)
    expect(page.locator('#logout2')).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text("Welcome Saikrishna")


#Note: To achieving auto retry.In playwright.So we need to install additional plugin 'pip install pytest-rerunfailures'.

#cmd: pytest .\playwright\test_flaky.py -s -v --headed --rerun 3 --reruns-delay 2