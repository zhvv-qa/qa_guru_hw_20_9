import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_settings():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()

@pytest.fixture
def open_browser_chrome(browser_settings):
    browser_settings.open('https://demoqa.com/automation-practice-form')
    return browser_settings