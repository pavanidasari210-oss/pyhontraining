from tkinter.font import names

import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_mouse_hover(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")
    page.locator("#hover-menu-trigger").hover()
    page.wait_for_timeout(5000)

def test_mouse_rightclick(page: Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    page.locator(".context-menu-one.btn.btn-neutral").click(button="right")
    page.wait_for_timeout(5000)

def test_mouse_Double_click(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    btncopy=page.get_by_role("button",name="Copy Text")
    btncopy.dblclick()
    page.wait_for_timeout(5000)

def test_mouse_drag_dropdown(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")
    source=page.locator("#drag-source")
    target=page.locator("#drop-zone")
    source.drag_to(target)
    page.wait_for_timeout(5000)
