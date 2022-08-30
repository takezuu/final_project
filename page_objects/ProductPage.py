from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    PATH = 'desktops/test'
    LIKE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    RIGHT_SIDEBAR = (By.CSS_SELECTOR, "#content div .col-sm-4")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".image-additional a img")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    UPLOAD_FILE_BUTTON = ((By.CSS_SELECTOR, "#button-upload222"), 'data-loading-text')
