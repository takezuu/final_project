from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class AdminPage(BasePage):
    PATH = 'admin'
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    LOGIN_PANEL = (By.CSS_SELECTOR, ".panel.panel-default")
    FOOTER_LINK = (By.CSS_SELECTOR, "#footer a")
    LOGIN_FIELD = LOGIN_FIELD = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_FIELD = ((By.CSS_SELECTOR, "#input-password"), 'type')

    @allure.step('Log in')
    def log_in(self, login, password):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys(login)
            self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
            self.browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='log_in')
            raise AssertionError("Авторизация не удалась")

    @allure.step('Add new product')
    def add_new_product(self, product_name, meta_teg, product_model):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#menu-catalog").click()
            WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-catalog > ul > "
                                                                                              "li:nth-child("
                                                                                              "2)"))).click()
            self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Add New']").click()
            self.browser.find_element(By.CSS_SELECTOR, "#input-name1").send_keys(product_name)
            self.browser.find_element(By.CSS_SELECTOR, "#input-meta-title1").send_keys(meta_teg)
            self.browser.find_element(By.CSS_SELECTOR, ".nav.nav-tabs > li:nth-child(2)").click()
            self.browser.find_element(By.CSS_SELECTOR, "#input-model").send_keys(product_model)
            self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Save']").click()
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='add_new_product')
            raise AssertionError("Новый продукт не добавлен")

    @allure.step('Check new product')
    def check_new_product(self, product_name):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#input-name").send_keys(product_name)
            self.browser.find_element(By.CSS_SELECTOR, "#button-filter").click()
            return self.browser.find_element(By.CSS_SELECTOR, "tbody tr .text-left").text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='check_new_product')
                raise AssertionError("Новый продукт не добавлен")

    @allure.step('Delete product')
    def delete_product(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "tbody .text-center input").click()
            self.browser.find_element(By.CSS_SELECTOR, "[data-original-title='Delete']").click()
            self.browser.switch_to.alert.accept()
            return self.browser.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        except NoSuchElementException:
            with allure.step('Screenshot'):
                allure.attach(body=self.browser.get_screenshot_as_png(),
                              name='delete_product')
                raise AssertionError("Продукт не удален")
