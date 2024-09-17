from pages.base_page import BasePage
from helpers.urls import BASE_URL
from selenium.webdriver.common.by import By
import allure


class MainLocators:
    TITLE = (By.CSS_SELECTOR, '[data-cy="home-categories-title"]')
    SEARCH = (By.CSS_SELECTOR, '[class="css-104mdwb"]')
    ANIMAL = (By.CSS_SELECTOR, '[data-path="zwierzeta"]')
    WORK = (By.CSS_SELECTOR, '[data-path="praca"]')
    APARTMENT = (By.CSS_SELECTOR, '[data-path="nieruchomosci"]')


class MainPage(BasePage, MainLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open page olx.com')
    def open(self):
        self.open_page(BASE_URL)

    @allure.step('That main page is opened')
    def assert_that_main_page_is_opened(self):
        assert self.get_element(self.TITLE)
        assert self.get_element(self.SEARCH)

    @allure.step('That category is visible')
    def assert_that_category_is_visible(self):
        assert self.get_element(self.ANIMAL)
        assert self.get_element(self.WORK)

    @allure.step('That apartment is visible')
    def assert_apartment_is_visible(self):
        assert self.get_element(self.APARTMENT)

