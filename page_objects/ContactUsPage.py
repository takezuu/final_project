from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
import config


class ContactUsPage(BasePage):
    ICON = (By.CSS_SELECTOR, ".fa.fa-phone")
    YOUR_NAME = "#input-name"
    E_MAIL = "#input-email"
    ENQUIRY = "#input-enquiry"
    SUBMIT = "[value='Submit']"
    MESSAGE = "#content > p"
    MESSAGE_NAME = "fieldset > div > div > div"
    CONTINUE = '#content > div > div > a'
    ADDRESS = '.panel-body > div > div > address'
    FRST_FIELD = 'fieldset > div:nth-child(2)'
    SECOND_FIELD = 'fieldset > div:nth-child(3)'
    THIRD_FIELD = 'fieldset > div:nth-child(4)'

    @allure.step('Open contact us page')
    def open_contacts_us(self, icon):
        try:
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(icon)).click()
        except TimeoutException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='contact_us_button')
            raise AssertionError("Не дождалcя возможности клика по кнопке")

    @allure.step('Fill contact us form')
    def fill_form(self, name, email, enquiry):
        try:
            self.browser.find_element(By.CSS_SELECTOR, name).send_keys(config.NAME)
            self.browser.find_element(By.CSS_SELECTOR, email).send_keys(config.EMAIL)
            self.browser.find_element(By.CSS_SELECTOR, enquiry).send_keys(config.ENQUIRY)
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='fill_form')
            raise AssertionError("Контактная форма не заполнена")

    @allure.step('Press submit button')
    def press_submit_button(self, submit):
        try:
            self.browser.find_element(By.CSS_SELECTOR, submit).click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='submit button')
            raise AssertionError("Кнопка SUBMIT не нажата")

    @allure.step('Get message')
    def get_message(self, message):
        return self.browser.find_element(By.CSS_SELECTOR, message).text

    @allure.step('Press continue button')
    def press_continue_button(self, continuebtn):
        try:
            self.browser.find_element(By.CSS_SELECTOR, continuebtn).click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='continue button')
            raise AssertionError("Кнопка CONTINUE не нажата")

    @allure.step('Get attribute')
    def get_attribute(self, required):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, required).get_attribute('class')
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get attribute')
            raise AssertionError("Атрибут не получен")

    @allure.step('Get address')
    def get_address(self, address):
        try:
            return self.browser.find_element(By.CSS_SELECTOR, address).text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='get address')
            raise AssertionError("Адресс не получен")
