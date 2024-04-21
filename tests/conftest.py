from selene import browser
import pytest


@pytest.fixture(scope='function',
                params=['mobile', 'desktop'])
def configure_browser(request):
    browser.config.base_url = 'https://github.com'
    if request.param == 'mobile':
        return request.getfixturevalue('mobile_view_size')
    elif request.param == 'desktop':
        return request.getfixturevalue('desktop_view_size')


@pytest.fixture(scope='function')
def mobile_view_size():
    browser.config.window_width = 375
    browser.config.window_height = 667
    return browser


@pytest.fixture(scope='function')
def desktop_view_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    return browser


@pytest.fixture(scope='function')
def configure_browser_desktop(desktop_view_size):
    desktop_view_size.config.base_url = 'https://github.com'
    return desktop_view_size


@pytest.fixture(scope='function')
def configure_browser_mobile(mobile_view_size):
    mobile_view_size.config.base_url = 'https://github.com'
    return mobile_view_size
