from pages.base_page import BasePage
from helpers.urls import BASE_URL
from selenium.webdriver.common.by import By
import allure
from locators.main_locators import MainLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
