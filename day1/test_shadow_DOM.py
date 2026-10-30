from playwright.sync_api import Page,expect
import pytest

def test_shadow_DOM(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")

    # Using CSS:
    #page.locator("#shadow-input").fill("welcome")

    #USing playwright locator
    page.get_by_role("textbox", name='shadow DOM input').fill("welcome")
    page.wait_for_timeout(5000)
