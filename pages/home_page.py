from helpers import BASE_URL, Assertions
from locators import HomePageOlxLocators
from pages import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage, HomePageOlxLocators, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def assert_that_home_page_is_open(self):
        assert self.get_element(self.SEARCH)
        assert self.get_element(self.SUBMIT_TAG)



