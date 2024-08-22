from pages import HomePage


def test_open_page(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.assert_that_home_page_is_open()