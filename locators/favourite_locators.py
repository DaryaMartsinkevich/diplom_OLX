from selenium.webdriver.common.by import By


class FavouriteLocators:
    ADS = (By.CSS_SELECTOR, '[data-testid="select-ads"]')
    SEARCHES = (By.CSS_SELECTOR, '[data-testid="select-search"]')
    VIEWING = (By.CSS_SELECTOR, '[data-testid="select-lastseen"]')