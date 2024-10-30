from selenium.webdriver.common.by import By


class LogoLocators:

    FACEBOOK = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button[1]/span/span/div')
    APPLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button[2]/span/span/div')
    GOOGLE = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/button[3]/span/span/div')
    TITLE = (By.XPATH, '//*[@id="__next"]/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/header/button[1]/span')
    EMAIL = (By.XPATH, '//*[@id="username"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    SUBMIT = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/button[2]/span/span')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/button[1]/span')
    SHOW_PASSWORD = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/form/div[2]/div/div/div/'
                               'div')
    REGISTER = (By.CSS_SELECTOR, '[data-testid="tabs"]')
    FACEBOOK_ACCESS = (By.XPATH, '//*[@id="u_0_0_Gd"]')
    APPLE_ACCESS = (By.XPATH, '//*[@id="sign_in_form"]')
    GOOGLE_ACCESS = (By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/'
                               'div/div/div/div/ul/li[1]/div')
    MY_ANNOUCEMENT = (By.XPATH, '//*[@id="mainContent"]/div[1]/div[2]/div[1]/div[1]/h3')
    GOOGLE_ACCOUNT = (By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/'
                                'section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')
    CONTINUE_GOOGLE = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span')
