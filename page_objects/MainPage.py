from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class MainPage(BasePage):
    SHOPPING_BUTTON = (By.CSS_SELECTOR, "#cart button")
    NAV_BAR = (By.CSS_SELECTOR, '.row')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, ".btn-group button")
    TOP_NAV_BAR = (By.CSS_SELECTOR, ".collapse.navbar-collapse.navbar-ex1-collapse")
    CAROUSEL = ((By.CSS_SELECTOR, ".swiper-container.swiper-container-horizontal"), 'id')

    @allure.step('Open reg form')
    def open_reg_form(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, ".dropdown").click()
            self.browser.find_element(By.CSS_SELECTOR, ".dropdown.open > ul > li > a").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='open_reg_form')
                raise AssertionError("Форма регистрации не открыта")

    @allure.step('Define currency')
    def define_currency(self):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle > strong").text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='define_currency')
                raise AssertionError("Валюта не определена")

    @allure.step('Change currency')
    def change_currency(self, currency):
        try:
            if currency == '$':
                self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
                self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name = 'EUR']").click()
            elif currency == '€':
                self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
                self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name='GBP']").click()
            elif currency == '£':
                self.browser.find_element(By.CSS_SELECTOR, ".btn-group").click()
                self.browser.find_element(By.CSS_SELECTOR, ".btn-group.open > ul > li > [name='USD']").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='change_currency')
                raise AssertionError("Валюта не изменилась")

    @allure.step('Compare currency')
    def compare_currency(self, currency, currency_2):
        assert currency != currency_2, 'Валюта не переключилась'
