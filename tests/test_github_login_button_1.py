import pytest
from selene import browser


def test_github_login_button_desktop(configure_browser):
    if configure_browser < 1012:
        pytest.skip(reason='too small window')
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_login_button_mobile(configure_browser):
    if configure_browser >= 1012:
        pytest.skip(reason='too big window')
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
