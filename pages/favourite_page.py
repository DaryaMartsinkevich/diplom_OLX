from pages.base_page import BasePage
from locators.favourite_locators import FavouriteLocators


class FavouritePage(BasePage, FavouriteLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_favourite_page_is_opened(self):
        assert self.get_element(self.ADS)
        assert self.get_element(self.SEARCHES)
        assert self.get_element(self.VIEWING)
