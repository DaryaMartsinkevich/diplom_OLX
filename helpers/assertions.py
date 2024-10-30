import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait, TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class Assertions:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Assert that text is visible")
    def assert_that_text_is_visible(self, selector, text):
        el = self.driver.find_element(selector)
        assert el.text == text

    @allure.step("Assert that element is visible")
    def assert_that_element_is_visible(self, selector):
        assert self.driver.find_element(selector)

    @allure.step("Assert that element is invisible")
    def assert_that_element_is_invisible(self, selector):
        try:
            self.driver.find_element(selector)
            assert False, f"Element '{selector}' was found, but it should be invisible."
        except NoSuchElementException:
            pass

    @allure.step("Assert that attribute is visible")
    def assert_that_attribute_is_visible(self, selector, attribute, value):
        el = self.driver.find_element(selector)
        assert el.get_attribute(attribute) == value

    @allure.step("Assert that attribute class is visible")
    def assert_that_attribute_class_is_visible(self, selector, value):
        self.assert_that_attribute_is_visible(selector, 'class', value)

    @allure.step("Assert that element contain text")
    def assert_that_element_containce_text(self, selector, value):
        element = self.driver.find_element(*selector)
        assert element.text == value, "Text from element, not the same"

    @allure.step('Assert that element is clickable')
    def assert_that_element_is_clickable(self, selector):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(selector))
            assert element is not None, f"Element with selector {selector} is not found."
        except TimeoutException:
            raise AssertionError(f"Element with selector {selector} is not clickable after 10 seconds.")

    @allure.step("Assert that element is not clickable")
    def assert_that_element_is_not_clickable(self, selector):
        with allure.step("Check element is not clickable"):
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((selector)))
                assert False, "Element is clickable"
            except TimeoutException:
                element = self.driver.find_element(selector)
                assert not element.is_enabled() or not element.is_displayed(), "Element is still interactable"