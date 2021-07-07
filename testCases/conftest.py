from selenium import webdriver
import pytest
from webdriver_manager import chrome, firefox
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        options = Options()
        # options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=chrome.ChromeDriverManager().install())
        print("Launching Chrome Browser.....")
    elif browser == 'firefox':
        # options = webdriver.FirefoxOptions()
        # options.add_argument(argument="--headless")
        # options.add_argument(argument="--disable-gpu")
        driver = webdriver.Firefox(executable_path=firefox.GeckoDriverManager().install())
        print("Launching Firefox Browser.....")
    else:
        # options = Options()
        # options.headless = True
        driver = webdriver.Chrome(executable_path=chrome.ChromeDriverManager().install())
        print("Launching Default: 'Chrome' Browser.....")
    driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rohit'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)