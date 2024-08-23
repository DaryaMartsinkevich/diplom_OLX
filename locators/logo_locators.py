from selenium.webdriver.common.by import By


class LogoLocators:

    FACEBOOK = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button[1]/span/span/div')
    APPLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button[2]/span/span/div')
    GOOGLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button[3]/span/span/div')
    TITLE = (By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/header/button[1]/span')
    USERNAME = (By.XPATH, '//*[@id="username"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    SUBMIT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/button[2]/span/span')
