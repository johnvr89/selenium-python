# tests/conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    # --- Configuración (Setup) ---
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # "yield" entrega el objeto driver a la función de prueba
    yield driver
    
    # --- Desmontaje (Teardown) ---
    print("\nCerrando el navegador...")
    driver.quit()