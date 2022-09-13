import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--base_url", default='http://192.168.8.113:8081/')
    parser.addoption("--browser_name", default="chrome", help="Choose browser")
    parser.addoption("--executor", default='192.168.8.113')
    parser.addoption("--bv")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                               options=options,
                               desired_capabilities={
                                   "BrowserName": browser_name,
                                   "browserVersion": version
                               }
                               )

    browser.maximize_window()

    yield browser
    browser.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
