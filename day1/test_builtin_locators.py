import pytest
import re
from playwright.sync_api import Page,expect

# page.get_by_alt_text() -----> It's useful to find out of images on the webpage like logos, images

# def test_verify_pw_locators(page: Page):
#     page.goto("https://demo.nopcommerce.com/")
#     page.wait_for_timeout(15000)
#     logo=page.get_by_alt_text("nopCommerce demo store")
#     expect(logo).to_be_visible()
#
# # page.get_by_text()
# def test_verify_text(page: Page):
#     page.goto("https://demo.nopcommerce.com/")
#     txt=page.get_by_text("Welcome to our store")
#     expect(txt).to_be_visible()

# page.get_by_role()

# def test_verify_role(page: Page):
#     page.goto("https://www.youtube.com/")
#     page.get_by_role("combobox",name="Search").fill("kalyani song")
#     page.get_by_role("button", name="Search", exact=True).click()
#     page.get_by_role("link",name=re.compile(r"KALYANI.*Shreya Ghoshal")).click()


import re
from playwright.sync_api import Page, expect


def test_verify_role(page: Page):
    page.goto(
        "https://www.youtube.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.get_by_role(
        "combobox",
        name="Search"
    ).fill("kalyani song")

    page.get_by_role(
        "button",
        name="Search",
        exact=True
    ).click()

    video = page.get_by_role(
        "link",
        name=re.compile(
            r"KALYANI.*Shreya Ghoshal",
            re.IGNORECASE
        )
    ).first

    expect(video).to_be_visible(timeout=20000)
    video.click()

    expect(page).to_have_url(
        re.compile(r".*youtube\.com/watch\?v=z5y8Clp_TdE.*"),
        timeout=20000
    )


