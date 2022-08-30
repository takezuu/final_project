from page_objects.ProductPage import ProductPage
import allure


@allure.feature('Product page')
@allure.title('Check the like button')
def test_clickable_of_like_button(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_clickable(ProductPage.LIKE_BUTTON)


@allure.feature('Product page')
@allure.title('Check the right column')
def test_right_sidebar_visibility_of_all_elements(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_visibility_of_all_elements_located(ProductPage.RIGHT_SIDEBAR)


@allure.feature('Product page')
@allure.title('Check image')
def test_presence_of_product_image(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_presence_of_element(ProductPage.PRODUCT_IMAGE)


@allure.feature('Product page')
@allure.title('Check add to cart button')
def test_visibility_of_add_to_cart_button(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_visibility_of_element(ProductPage.ADD_TO_CART_BUTTON)


@allure.feature('Product page')
@allure.title('Check upload file button\'s attribute')
def test_upload_file_button_for_element_attribute(browser, base_url):
    ProductPage(browser).open_url(base_url, ProductPage.PATH)
    ProductPage(browser).check_element_attribute(ProductPage.UPLOAD_FILE_BUTTON)
