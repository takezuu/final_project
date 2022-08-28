import config
from page_objects.LoginPage import LoginPage
import allure


@allure.feature('LoginPage')
@allure.title('Open login page')
def test_open_login_page(browser, base_url):
    LoginPage(browser).open_url(base_url)
    LoginPage(browser).open_login_page(LoginPage.MY_ACCOUNT, LoginPage.LOGIN)
    url = LoginPage(browser).get_url()
    assert url == 'http://192.168.8.113:8081/index.php?route=account/login', 'Неверная страница'


@allure.feature('LoginPage')
@allure.title('Login page warning')
def test_warning_of_login_page(browser, base_url):
    LoginPage(browser).open_url(base_url)
    LoginPage(browser).open_login_page(LoginPage.MY_ACCOUNT, LoginPage.LOGIN)
    LoginPage(browser).click_button(LoginPage.LOGIN_BUTTON)
    text = LoginPage(browser).get_text(LoginPage.WARNING)
    assert text == ' Warning: No match for E-Mail Address and/or Password.', 'Предупрждение не появилось'


@allure.feature('LoginPage')
@allure.title('Failed login')
def test_warning_of_login_page(browser, base_url):
    LoginPage(browser).open_url(base_url)
    LoginPage(browser).open_login_page(LoginPage.MY_ACCOUNT, LoginPage.LOGIN)
    LoginPage(browser).fill_login_form(LoginPage.EMAIL, LoginPage.PASSWORD, config.EMAIL, config.LOGIN_PASSWORD)
    LoginPage(browser).click_button(LoginPage.LOGIN_BUTTON)
    text = LoginPage(browser).get_text(LoginPage.WARNING)
    assert text == 'Warning: No match for E-Mail Address and/or Password.', 'Предупрждение не появилось'


@allure.feature('LoginPage')
@allure.title('Open link forgotten password')
def test_warning_of_login_page(browser, base_url):
    LoginPage(browser).open_url(base_url)
    LoginPage(browser).open_login_page(LoginPage.MY_ACCOUNT, LoginPage.LOGIN)
    LoginPage(browser).click_button(LoginPage.FORGOTTEN)
    url = LoginPage(browser).get_url()
    assert url == 'http://192.168.8.113:8081/index.php?route=account/forgotten', 'Cтраница восстановления пароля не открылась'


@allure.feature('LoginPage')
@allure.title('Check text of new customer')
def test_warning_of_login_page(browser, base_url):
    LoginPage(browser).open_url(base_url)
    LoginPage(browser).open_login_page(LoginPage.MY_ACCOUNT, LoginPage.LOGIN)
    url = LoginPage(browser).get_text(LoginPage.NEW_CUSTOMER_TEXT)
    assert url == 'New Customer\n''Register Account\n''By creating an account you will be able to shop faster, be up to date on an '"order's status, and keep track of the orders you have previously made.\n"'Continue', 'Неправильный текст в разделе новый покупатель'
