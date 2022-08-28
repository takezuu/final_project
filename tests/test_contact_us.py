from page_objects.ContactUsPage import ContactUsPage
import allure


@allure.feature('ContactUsPage')
@allure.title('Fill form')
def test_send_message(browser, base_url):
    ContactUsPage(browser).open_url(base_url)
    ContactUsPage(browser).open_contacts_us(ContactUsPage.ICON)
    ContactUsPage(browser).fill_form(ContactUsPage.YOUR_NAME, ContactUsPage.E_MAIL, ContactUsPage.ENQUIRY)
    ContactUsPage(browser).press_submit_button(ContactUsPage.SUBMIT)
    message = ContactUsPage(browser).get_message(ContactUsPage.MESSAGE)
    assert message == 'Your enquiry has been successfully sent to the store owner!', 'Cообщение не отправлено'


@allure.feature('ContactUsPage')
@allure.title('Failed fill form')
def test_fail_send_message(browser, base_url):
    ContactUsPage(browser).open_url(base_url)
    ContactUsPage(browser).open_contacts_us(ContactUsPage.ICON)
    ContactUsPage(browser).press_submit_button(ContactUsPage.SUBMIT)
    message = ContactUsPage(browser).get_message(ContactUsPage.MESSAGE_NAME)
    assert message == 'Name must be between 3 and 32 characters!', 'Cообщение не отправлено'


@allure.feature('ContactUsPage')
@allure.title('Return to home page')
def test_return_to_home_page(browser, base_url):
    ContactUsPage(browser).open_url(base_url)
    ContactUsPage(browser).open_contacts_us(ContactUsPage.ICON)
    ContactUsPage(browser).fill_form(ContactUsPage.YOUR_NAME, ContactUsPage.E_MAIL, ContactUsPage.ENQUIRY)
    ContactUsPage(browser).press_submit_button(ContactUsPage.SUBMIT)
    ContactUsPage(browser).press_continue_button(ContactUsPage.CONTINUE)
    url = ContactUsPage(browser).get_url()
    assert url == 'http://192.168.8.113:8081/index.php?route=common/home', 'Не верная страница'


@allure.feature('ContactUsPage')
@allure.title('Check adress of store')
def test_check_address_of_store(browser, base_url):
    ContactUsPage(browser).open_url(base_url)
    ContactUsPage(browser).open_contacts_us(ContactUsPage.ICON)
    address = ContactUsPage(browser).get_address(ContactUsPage.ADDRESS)
    assert address == 'Address 1', 'Адрес не верный'


@allure.feature('ContactUsPage')
@allure.title('Required fields')
def test_check_of_required_fields(browser, base_url):
    ContactUsPage(browser).open_url(base_url)
    ContactUsPage(browser).open_contacts_us(ContactUsPage.ICON)
    attribute_1 = ContactUsPage(browser).get_attribute(ContactUsPage.FRST_FIELD)
    attribute_2 = ContactUsPage(browser).get_attribute(ContactUsPage.SECOND_FIELD)
    attribute_3 = ContactUsPage(browser).get_attribute(ContactUsPage.THIRD_FIELD)
    assert attribute_1 == attribute_2 == attribute_3 == 'form-group required', 'Не все поля обязательны'
