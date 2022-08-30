from page_objects.UserRegistrationPage import UserRegistrationPage
from page_objects.MainPage import MainPage
import allure


@allure.feature('Registration page')
@allure.title('Continue button')
def test_clickable_of_continue_button(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_clickable(UserRegistrationPage.CONTINUE_BUTTON)


@allure.feature('Registration page')
@allure.title('Account section')
def test_account_section_visibility_of_all_elements(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_visibility_of_all_elements_located(UserRegistrationPage.ACCOUNT_SECTION)


@allure.feature('Registration page')
@allure.title('Login page link')
def test_presence_of_login_page_link(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_presence_of_element(UserRegistrationPage.LOGIN_PAGE_LINK)


@allure.feature('Registration page')
@allure.title('Agree check box')
def test_visibility_of_agree_check_box(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_visibility_of_element(UserRegistrationPage.AGREE_CHECK_BOX)


@allure.feature('Registration page')
@allure.title('Right column')
def test_right_column_for_element_attribute(browser, base_url):
    UserRegistrationPage(browser).open_url(base_url, UserRegistrationPage.PATH)
    UserRegistrationPage(browser).check_element_attribute(UserRegistrationPage.RIGHT_COLUMN)


@allure.feature('Registration page')
@allure.title('Registration of new user')
def test_registration_of_new_user(browser, base_url):
    MainPage(browser).open_url(base_url)
    MainPage(browser).open_reg_form()
    form_text = UserRegistrationPage(browser).fill_form(UserRegistrationPage.data)
    assert form_text == 'Your Account Has Been Created!', 'Аккаунт не зарегистрирован'
