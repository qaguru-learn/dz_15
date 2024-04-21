import pytest

from selene import browser


@pytest.mark.parametrize('configure_browser', [(1920, 1080)], indirect=True)
def test_github_login_button_desktop(configure_browser):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('configure_browser', [(375, 667)], indirect=True)
def test_github_login_button_mobile(configure_browser):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
