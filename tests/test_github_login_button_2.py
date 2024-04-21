import pytest


@pytest.mark.parametrize('configure_browser', ['desktop'], indirect=True)
def test_github_login_button_desktop(configure_browser):
    browser = configure_browser
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('configure_browser', ['mobile'], indirect=True)
def test_github_login_button_mobile(configure_browser):
    browser = configure_browser
    browser.open('/')
    browser.element('.js-details-target.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
