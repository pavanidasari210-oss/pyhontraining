from playwright.sync_api import Page, expect
import pytest
@pytest.mark.skip
def test_css_id(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("T-shirts")  #   tag id ---------->Tag#ID (Tag is optional)
    page.get_by_role("button",name="Search").click()
    page.wait_for_timeout(5000)

def test_css_class(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input.search-box-text").fill("T-shirts")  #   tag class ---------->Tag.class (Tag is optional)
    page.get_by_role("button",name="Search").click()
    page.wait_for_timeout(5000)

def test_css_attribute(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input[value='Search store']").fill("T-shirts")  # tag Attribute ---------->Tag[Attribute='value'] (Tag is optional)
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(5000)

