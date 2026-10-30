import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_keyboard_actions(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input1=page.locator("#input1")

    #1. focus on input1 box
    input1.focus()

    #2. provide the text in input1 using keyboard method
    page.keyboard.insert_text("Hello")

    #3.ctrl+A
    page.keyboard.press("Control+A")

    #4. ctrl+C
    page.keyboard.press("Control+C")

    #5. press Tab key 2 times to navigate/focus on input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    #6.ctrl+v - to paste the text inside the 2 nd inputbox-input2
    page.keyboard.press("Control+V")

    page.wait_for_timeout(5000) 