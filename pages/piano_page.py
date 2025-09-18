# pages/piano_page.py

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import TestData

class PianoPage(BasePage):
    # --- Locators (sin cambios) ---
    #KEY_DO = (By.CSS_SELECTOR, "span[data-key='84']")
    #KEY_RE = (By.CSS_SELECTOR, "span[data-key='89']")
    #KEY_FA = (By.CSS_SELECTOR, "span[data-key='73']")
    #KEY_SOL = (By.CSS_SELECTOR, "span[data-key='79']")
    #KEY_LA = (By.CSS_SELECTOR, "span[data-key='80']")
    #KEY_SI = (By.CSS_SELECTOR, "span[data-key='219']")

    KEY_DO = (By.XPATH, "//span[text()='do']")
    KEY_RE = (By.XPATH, "//span[text()='re']")
    KEY_FA = (By.XPATH, "//span[text()='fa']")
    KEY_SOL = (By.XPATH, "//span[text()='sol']")
    KEY_LA = (By.XPATH, "//span[text()='la']")
    KEY_SI = (By.XPATH, "//span[text()='si']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.PIANO_URL)
        self.driver.maximize_window()

    def tocar_do(self):
        self.click(self.KEY_DO)
        time.sleep(1)

    def tocar_re(self):
        self.click(self.KEY_RE)
        time.sleep(1)

    def tocar_fa(self):
        self.click(self.KEY_FA)
        time.sleep(1)    

    def tocar_sol(self):
        self.click(self.KEY_SOL)
        time.sleep(1)
    
    def tocar_la(self):
        self.click(self.KEY_LA)
        time.sleep(1)

    def tocar_si(self):
        self.click(self.KEY_SI)
        time.sleep(1)

    def tocar_nueva_melodia(self):
        """
        Toca una nueva melodía en el piano.
        """
        print("Tocando una nueva melodía...")
        self.tocar_si()
        self.tocar_si()
        self.tocar_do()
        self.tocar_re()
        self.tocar_re()
        self.tocar_do()
        self.tocar_si()
        self.tocar_la()
        self.tocar_sol()
        self.tocar_sol()
        self.tocar_la()
        self.tocar_si()

        self.tocar_la()
        self.tocar_sol()
        self.tocar_sol()
        self.tocar_la()
        self.tocar_si()
        self.tocar_sol()
        self.tocar_la()
        self.tocar_si()
        self.tocar_do()
        self.tocar_si()
        self.tocar_sol()
        self.tocar_la()
        self.tocar_si()
        self.tocar_do()
        self.tocar_si()
        self.tocar_sol()
        self.tocar_sol()
        #self.tocar_fa()
        #self.tocar_re()         
        time.sleep(1) # Pausa al final para escuchar la melodía

    def tocar_melodia_estrellita(self, veces=1):
        """
        Toca la secuencia de notas de la melodía un número determinado de veces.
        """
        # Bucle que se repetirá según el número que reciba
        for i in range(veces):
            print(f"Tocando melodía (Repetición {i+1}/{veces})...")
            self.tocar_si()
            self.tocar_si()
            self.tocar_do()
            self.tocar_re()
            self.tocar_re()
            self.tocar_do()
            self.tocar_si()
            self.tocar_la()
            self.tocar_sol()
            self.tocar_sol()
            self.tocar_la()
            self.tocar_si()
            self.tocar_si()
            self.tocar_la()
            self.tocar_la()
            time.sleep(2) # Pausa al final para escuchar la melodía
