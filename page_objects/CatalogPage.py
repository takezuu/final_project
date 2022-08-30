from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    PATH = 'desktops'
    LIST_BUTTON = (By.CSS_SELECTOR, "#list-view")
    CONTENT_AREA = (By.CSS_SELECTOR, "#content")
    FOOTER = (By.CSS_SELECTOR, "footer")
    LEFT_COLUMN = (By.CSS_SELECTOR, "#column-left")
    PRODUCT_ICON = ((By.CSS_SELECTOR, "#content div div img"), 'class')
