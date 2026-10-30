# In playwright by default page fixture is available.
from playwright.sync_api import Page,expect

from playwright.sync_api import Page, expect

URL = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"



def test_verify_pageUrl(page:Page):
    page.goto(URL)
    page.wait_for_timeout(5000)
    expect(page).to_have_url(URL)

def test_verifyTitle(page: Page):
    page.goto(URL)
    page.wait_for_timeout(5000)
    expect(page).to_have_title("Automation Testing Practice")
    page.close()

# def test_verify_pwlocators(page:Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     page.wait_for_timeout(5000)
#     checkbox=page.get_by_role('checkbox',name="Verify you are human")
#     checkbox.check()
#     logo=page.get_by_alt_text("Picture for category Clothing")
#     expect(logo).to_be_visible()
# def test_pageTest(page: Page):
#     page.goto("https://www.youtube.com/")
#     page.wait_for_timeout(2000)
#     # locator=page.get_by_role("textbox",name="Username")
#     # expect(locator).to_be_visible()
#     # page.fill("Username","Admin")
#     # page.close()
#     page.get_by_placeholder("search").fill("neso academy python programming")
#     #page.get_by_placeholder("Password").fill("admin123")
#     button= page.get_by_title("Search")
#     button.click()
#     page.wait_for_timeout(5000)
#     #expect(page.get_by_role("heading",name="Dashboard")).to_have_text("Dashboard")



