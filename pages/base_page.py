class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, selector):
        return self.driver.find_element(*selector)

    def click(self, selector):
        element = self.driver.find_element(*selector)
        element.click()

    def input_text(self, selector, text):
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def add_cookies(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def delete_cookies(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.remove_cookie(cookie)


