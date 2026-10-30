import pytest
from playwright.sync_api import sync_playwright,Page,expect

def test_file_upload(page: Page):
    page.goto("https://www.sreenidhirajakrishnan.com/practice")
    page.locator("#file-upload").set_input_files("playwright\kalyani.txt")
    page.wait_for_timeout(10000)