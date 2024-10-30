from pages.base_page import BasePage
from locators.login_locators import LogoLocators
import allure
from selenium.webdriver.common.by import By


class LogoPage(BasePage, LogoLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Logo page is opened")
    def assert_that_logo_page_is_opened(self):
        assert self.get_element(self.REGISTER)

    @allure.step("Login by Facebook")
    def login_by_facebook(self):
        self.click(self.FACEBOOK)

    @allure.step("Login by Apple")
    def login_by_apple(self):
        self.click(self.APPLE)

    @allure.step("Login by Google")
    def login_by_google(self):
        self.click(self.GOOGLE)
        self.click(self.GOOGLE_ACCOUNT)
        self.click(self.CONTINUE_GOOGLE)

    @allure.step("Entering email")
    def enter_email(self):
        self.fill(self.EMAIL, 'daryamartsinkevich@gmail.com')

    @allure.step("Entering password")
    def enter_password(self):
        self.fill(self.PASSWORD, 'Red2665642')

    @allure.step("Click on 'Zaloguj się' button ")
    def login(self):
        self.click(self.SUBMIT)

    @allure.step("Login is correct")
    def assert_that_login_is_correct(self):
        assert self.get_element(self.EMAIL)
        assert self.get_element(self.PASSWORD)
        assert self.get_element(self.SUBMIT)

    @allure.step("Login is not correct")
    def assert_login_is_not_correct(self):
        self.fill(self.EMAIL, 'solnce.voda@gmail.com')
        self.fill(self.PASSWORD, 'qwerty')
        self.login()
        assert self.get_element(self.SUBMIT)

    def get_error_message(self):
        return self.input_text(By.CLASS_NAME, 'error-message').text

    @allure.step("Assert Facebook page")
    def assert_login_facebook(self):
        assert self.get_element(self.FACEBOOK_ACCESS)

    @allure.step("Assert Apple page")
    def assert_login_apple(self):
        assert self.get_element(self.APPLE_ACCESS)

    @allure.step("Assert Google page")
    def assert_login_google(self):
        assert self.get_element(self.GOOGLE_ACCESS)

    @allure.step("Forgot password")
    def forgot_password(self):
        self.click(self.FORGOT_PASSWORD)

    @allure.step("Login page is opened")
    def assert_that_login_page_is_opened(self):
        assert self.get_element(self.MY_ANNOUCEMENT)
