import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.desktops_page import DesktopsPage
from pages.card_product_page import CardProductPage
from pages.admin_page import AdminPage
from pages.tablets_page import TabletsPage
from pages.customers_page import CustomerPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)

    elif browser == "ie":
        driver = webdriver.Ie()

    elif browser == "remote":
        capabilities = {
            "acceptInsecureCerts": True,
            "browserName": "firefox",
            "version": "61.0",
            "enableVNC": True,
            "enableVideo": False,
            "session-attempt-timeout": "2m",
            "name": "OpenCart"
        }
        driver = webdriver.Remote(command_executor="http://10.5.29.233:4444/wd/hub", desired_capabilities=capabilities)

    # elif browser == "remote":
    #     capabilities = {
    #         "browserName": "chrome",
    #         "version": "73.0",
    #         "enableVNC": True,
    #         "enableVideo": False
    #     }
    #     driver = webdriver.Remote(command_executor="http://10.5.29.233:4444/wd/hub", desired_capabilities=capabilities)

    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox, ie or remote")

    driver.maximize_window()

    request.addfinalizer(driver.quit)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture()
def main_page(browser):
    page = MainPage(browser, base_url=browser.current_url + "/index.php?route=account/login")
    page.go_to()
    return page


@pytest.fixture()
def login_page(browser):
    page = LoginPage(browser, base_url=browser.current_url + "/index.php?route=account/login")
    page.go_to()
    return page


@pytest.fixture()
def desktops_page(browser):
    page = DesktopsPage(browser, base_url=browser.current_url + "/index.php?route=product/category&path=20")
    page.go_to()
    return page


@pytest.fixture()
def card_product_page(browser):
    page = CardProductPage(browser,
                           base_url=browser.current_url + "/index.php?route=product/product&path=57&product_id=49")
    page.go_to()
    return page


@pytest.fixture()
def admin_page(browser):
    page = AdminPage(browser, base_url=browser.current_url + "/admin")
    page.go_to()
    return page


@pytest.fixture()
def tablets_page(browser):
    page = TabletsPage(browser, base_url=browser.current_url + "/index.php?route=product/category&path=57")
    page.go_to()
    return page


@pytest.fixture()
def customer_page(browser):
    page = CustomerPage(browser, base_url=browser.current_url + "/admin")
    page.go_to()
    return page
