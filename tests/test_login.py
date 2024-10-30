import time
from os import times

import allure
from elements import HeaderElement
from pages.login_page import LogoPage
from pages.main_page import MainPage


@allure.feature("Login page")
@allure.title("Open login page")
def test_open_login(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_main_page_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_account()

    logo_page = LogoPage(driver)
    logo_page.assert_that_logo_page_is_opened()


@allure.feature("Login page")
@allure.title("Open my account")
def test_login_success(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_main_page_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_account()

    logo_page = LogoPage(driver)
    logo_page.enter_email()
    logo_page.enter_password()
    logo_page.login()
    logo_page.assert_that_login_page_is_opened()


@allure.feature("Login page")
@allure.title("Login is not correct")
def test_login_failure(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_main_page_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_account()

    logo_page = LogoPage(driver)
    logo_page.assert_that_logo_page_is_opened()


def test_login_with_facebook(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()
    main_page.assert_that_main_page_is_opened()

    # header_element = HeaderElement(driver)
    # header_element.open_account()
    #
    # logo_page = LogoPage(driver)
    # logo_page.login_by_google()
    # logo_page.assert_that_login_page_is_opened()

