from page_objects.MainPage import MainPage
import allure


@allure.feature('Main page')
@allure.title('Shopping button')
def test_clickable_of_shopping_button(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_clickable(MainPage.SHOPPING_BUTTON)


@allure.feature('Main page')
@allure.title('Navigation bar')
def test_of_all_elements_nav_bar(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_visibility_of_all_elements_located(MainPage.NAV_BAR)


@allure.feature('Main page')
@allure.title('Currency button')
def test_presence_of_currency_button(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_presence_of_element(MainPage.CURRENCY_BUTTON)


@allure.feature('Main page')
@allure.title('Top navigation bar')
def test_visibility_of_top_navigation_bar(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_visibility_of_element(MainPage.TOP_NAV_BAR)


@allure.feature('Main page')
@allure.title('Carousel\'s attribute')
def test_carousel_for_element_attribute(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).check_element_attribute(MainPage.CAROUSEL)


@allure.feature('Main page')
@allure.title('Change currency')
def test_change_currency(browser, base_url):
    MainPage(browser).open_url(base_url)
    currency = MainPage(browser).define_currency()
    MainPage(browser).change_currency(currency)
    currency_2 = MainPage(browser).define_currency()
    MainPage(browser).compare_currency(currency, currency_2)
