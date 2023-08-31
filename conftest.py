import datetime
import allure
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options






@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome()
    driver.maximize_window()
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot {datetime.today()}', attachment_type=allure.attachment_type.PNG)
    yield driver
    driver.close()
    driver.quit()



