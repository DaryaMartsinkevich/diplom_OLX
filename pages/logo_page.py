from pages.base_page import BasePage
from locators.logo_locators import LogoLocators


class LogoPage(BasePage, LogoLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_logo_page_is_opened(self):
        assert self.get_element(self.FACEBOOK)
        assert self.get_element(self.APPLE)
        assert self.get_element(self.GOOGLE)
        assert self.get_element(self.USERNAME)
        assert self.get_element(self.PASSWORD)