import pytest
from playwright.sync_api import Page,expect

# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
url= "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"

def test_verify_alt_text(page: Page):
    page.goto(url)
    logo=page.get_by_alt_text("logo image")
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)
    page.close()

# page.get_by_text() to locate by text content.
def test_verify_get_by_text(page: Page):
    page.goto(url)
    logo=page.get_by_text("Hover over these elements to see their titles:")
    expect(logo).to_be_visible()
    page.wait_for_timeout(5000)
    page.close()

# page.get_by_role() to locate by explicit and implicit accessibility attributes.

def test_verify_get_by_role(page: Page):
    page.goto(url)
    data=page.get_by_role("textbox",name="Username")
    data.fill("Saikrishna")
    expect(data).to_have_value("Saikrishna")
    page.wait_for_timeout(5000)
    page.close()

# page.get_by_label() to locate a form control by associated label's text.

def test_verify_get_by_label(page: Page):
    page.goto(url)
    data=page.get_by_label("email")
    data.fill("saikrishna.tarani@gmail.com")
    expect(data).to_have_value("saikrishna.tarani@gmail.com")
    page.wait_for_timeout(5000)
    page.close()

# page.get_by_placeholder() to locate an input by placeholder.
def test_verify_get_by_placeholder(page: Page):
    page.goto(url)
    data=page.get_by_placeholder("Search products...")
    data.fill("Samsung")
    expect(data).to_have_value("Samsung")
    page.wait_for_timeout(5000)
    page.close()

# page.get_by_title() to locate an element by its title attribute.
def test_verify_get_by_title(page: Page):
    page.goto(url)
    title=page.get_by_title("Home page link")
    expect(title).to_have_text("Home")
    page.wait_for_timeout(5000)
    page.close()

# page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).
def test_verify_get_by_test_id(page: Page):
    page.goto(url)
    name=page.get_by_test_id("profile-email")
    expect(name).to_have_text("john.doe@example.com")
    page.wait_for_timeout(5000)
    page.close()