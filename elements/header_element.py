from pages.base_page import BasePage
from locators.header_locators import HeaderLocators


class HeaderElement(BasePage, HeaderLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_favourite(self):
        self.click(self.FAVOURITE)

    def open_account(self):
        self.click(self.ACCOUNT)

    def open_annoncement(self):
        self.click(self.ANNOUCEMENT)
