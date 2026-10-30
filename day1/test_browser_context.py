import pytest
from playwright.sync_api import sync_playwright,Playwright,Page,expect

# context--->context (user profiles)--->Page (or) pages
# Browser---> chromium,firefox,webkit like any instance...
# Page---->  on context we can create/open tab,window,popup

def test_browser_context(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()  #created Page-1
    page2=context.new_page()  #created Page-2

    #Note: The advantage of creating multiple pages is we can work with multiple url's/Applications at a time or parallely.
    #But if I use only one page or one page instance, you cannot work with the both URLs parallelly at a time

    page1.goto("https://playwright.dev/python/")
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright Python")
    page1.wait_for_timeout(5000)
    page2.goto("https://www.opencart.com/index.php?route=cms/demo", wait_until="domcontentloaded")
    expect(page2).to_have_title("OpenCart - Demo")
    page2.wait_for_timeout(5000)
