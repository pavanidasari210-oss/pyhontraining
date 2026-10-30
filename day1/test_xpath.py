import pytest
from playwright.sync_api import Page, expect


def test_xpath_locator(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    #1.Absolute Xpath (Full path) Note: we mostly prefer for 'relative xpath' not Absolute xpath
    logo=page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)

    #2. Relative xpath (partial path)  syntax: //tagname[@attribute='value']
def test_xpath_locator1(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()
    page.wait_for_timeout(2000)

    #3.xpath with contains()
