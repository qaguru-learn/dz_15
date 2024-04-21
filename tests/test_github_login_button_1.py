import pytest


def test_github_login_button_desktop(configure_browser):
    if configure_browser.config.window_width < 1012:
        pytest.skip(reason='too small window')
    browser = configure_browser
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_login_button_mobile(configure_browser):
    if configure_browser.config.window_width >= 1012:
        pytest.skip(reason='too big window')
    browser = configure_browser
    browser.open('/')
    browser.element('.js-details-target.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
