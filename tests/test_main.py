import allure

from pages.main_page import MainPage
from elements.header_element import HeaderElement
from pages.favourite_page import FavouritePage
from pages.logo_page import LogoPage


@allure.feature("Main page")
@allure.title("Open main page")
def test_open_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_main_page_is_opened()


@allure.feature("Main page")
@allure.title("Open page categories")
def test_categories(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_category_is_visible()


@allure.feature("Main page")
@allure.title("Visible categories")
def test_visible_categories(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_apartment_is_visible()


@allure.feature("Main page")
@allure.title("Open page favourite")
def test_open_favourite(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_main_page_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_favourite()

    favourite_page = FavouritePage(driver)
    favourite_page.assert_that_favourite_page_is_opened()


@allure.feature("Main page")
@allure.title("Open logo page")
def test_open_logo(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_main_page_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_account()

    logo_page = LogoPage(driver)
    logo_page.assert_that_logo_page_is_opened()





