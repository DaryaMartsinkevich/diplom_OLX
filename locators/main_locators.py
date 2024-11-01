from selenium.webdriver.common.by import By


class MainLocators:
    ALERT = (By.XPATH, '//button[contains(text(), "Akceptuj wszystkie")]')
    TITLE = (By.CSS_SELECTOR, '[data-cy="home-categories-title"]')
    SEARCH = (By.CSS_SELECTOR, '[class="css-104mdwb"]')
    ANIMAL = (By.CSS_SELECTOR, '[data-path="zwierzeta"]')
    WORK = (By.CSS_SELECTOR, '[data-path="praca"]')
    APARTMENT = (By.CSS_SELECTOR, '[data-path="nieruchomosci"]')
    ELECTRONICS = (By.CSS_SELECTOR, '[data-path="elektronika"]')
    FASHION = (By.CSS_SELECTOR, '[data-testid="cat-87"]')
    SPORTS = (By.CSS_SELECTOR, '[data-testid="cat-767"]')
    MUSIC = (By.CSS_SELECTOR, '[data-testid="cat-751"]')
    HEALTH = (By.CSS_SELECTOR, '[data-testid="cat-3647"]')
    SERVICES = (By.CSS_SELECTOR, '[data-testid="cat-4371"]')
    ANNOUCEMENT_TOP = (By.XPATH, '//*[@id="searchmain-container"]/div[3]/div/h2')
    OLX_BIZNES = (By.CSS_SELECTOR, '[data-testid="banner-btn"]')
    FIRMA_NA_OLX = (By.CSS_SELECTOR, '[class*="text-4xl sm:text-5xl font-bold"]')
    FACEBOOK_SOCIAL_NETWORK = (By.CSS_SELECTOR, '[href="https://www.facebook.com/olx.polska"]')
    INSTAGRAM_SOCIAL_NETWORK = (By.CSS_SELECTOR, '[data-testid="instagram"]')
    YOUTUBE_SOCIAL_NETWORK = (By.CSS_SELECTOR, '[data-testid="youtube"]')
    LINKEDIN_SOCIAL_NETWORK = (By.CSS_SELECTOR, '[data-testid="linkedIn"]')
    PINTEREST_SOCIAL_NETWORK = (By.CSS_SELECTOR, '[data-testid="pinterest"]')
    MOBILE_OLX = (By.CSS_SELECTOR, 'a[title="Aplikacje mobilne OLX.pl"]')
    HELP_OLX = (By.CSS_SELECTOR, 'a[title="Pomoc"]')
    BLOG = (By.CSS_SELECTOR, 'a[title="Blog"]')
    GOOGLE_PLAY = (By.XPATH, '//*[@id="footerContent"]/div/div[1]/div/ul/li[1]/a')
    APP_STORE = (By.XPATH, '//*[@id="footerContent"]/div/div[1]/div/ul/li[2]/a/img')
