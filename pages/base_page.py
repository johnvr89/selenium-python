# pages/base_page.py

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )
    
    def click(self, locator, time=10):
        element = self.find_element(locator, time)
        # Crea una cadena de acciones para hacer clic en el elemento y la ejecuta
        ActionChains(self.driver).click(element).perform()