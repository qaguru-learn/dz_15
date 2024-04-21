import pytest


def test_github_login_button_desktop(configure_browser_desktop):
    browser = configure_browser_desktop
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_login_button_mobile(configure_browser_mobile):
    browser = configure_browser_mobile
    browser.open('/')
    browser.element('.js-details-target.Button--medium').click()
    browser.element('.HeaderMenu-link--sign-in').click()
