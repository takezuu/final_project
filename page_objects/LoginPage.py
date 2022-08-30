from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure


class LoginPage(BasePage):
    MY_ACCOUNT = (By.CSS_SELECTOR, '.list-inline > .dropdown')
    LOGIN = (By.CSS_SELECTOR, '.list-inline > .dropdown > ul > li:nth-child(2)')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value='Login']")
    WARNING = (By.CSS_SELECTOR, '#account-login > div')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN = (By.CSS_SELECTOR, '#content > div > div:nth-child(2) > div > form > div:nth-child(2) > a')
    NEW_CUSTOMER_TEXT = (By.CSS_SELECTOR, '#content > div  > div > div')

    @allure.step('Open login page')
    def open_login_page(self, my_account, login):
        try:
            self.browser.find_element(*my_account).click()
            self.browser.find_element(*login).click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='open_login_page')
            raise AssertionError("Не открыта страница входа")

    @allure.step('Click button')
    def click_button(self, button):
        try:
            self.browser.find_element(*button).click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='click_button')
            raise AssertionError("Кнопка не нажата")

    @allure.step('Get text')
    def get_text(self, warning):
        try:
            return self.browser.find_element(*warning).text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check_warning')
            raise AssertionError("Нет предупреждения")

    @allure.step('Fill login form')
    def fill_login_form(self, email_selector, password_selector, email, password):
        try:
            self.browser.find_element(*email_selector).send_keys(email)
            self.browser.find_element(*password_selector).send_keys(password)
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='fill login form')
            raise AssertionError("Форма логина не заполнена")
