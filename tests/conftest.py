from selene import browser
import pytest


@pytest.fixture(scope='function',
                params=[(375, 667), (1920, 1080)])
def configure_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield width

    browser.quit()


@pytest.fixture(scope='function')
def configure_browser_mobile():
    browser.config.window_width = 375
    browser.config.window_height = 667
    yield
    browser.quit()


@pytest.fixture(scope='function')
def configure_browser_desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
