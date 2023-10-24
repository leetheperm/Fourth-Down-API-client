import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    # Go to the starting url before each test.
    page.goto("https://fourthdown.azurewebsites.net")
    yield


def test_site_is_live(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://fourthdown.azurewebsites.net/")