"""Minimal self-check for the image: does Chromium actually launch?
Run inside the built image: docker run --rm -i <image> python3 - < smoke_test.py
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("about:blank")
    browser.close()

print("chromium OK")
