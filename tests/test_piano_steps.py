import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from pytest_bdd import scenario, given, when, then, parsers
from pages.piano_page import PianoPage

# --- Conecta el escenario del .feature con este archivo ---
# --- Escenario 1 ---
@scenario('../features/piano.feature', 'Tocar una melodía simple en el piano')
def test_play_piano_once():
    """Función de prueba para el primer escenario."""
    pass

# --- Escenario 2 ---
@scenario('../features/piano.feature', 'Tocar una melodía 2 veces en el piano')
def test_play_piano_twice():
    """Función de prueba para el segundo escenario."""
    pass

# --- Escenario 3 ---
@scenario('../features/piano.feature', 'Tocar varias melodías en el piano')
def test_play_piano_multiple():
    """Función de prueba para el tercer escenario."""
    pass

# --- Implementación de los pasos ---

@given('el usuario está en el piano virtual de Musicca')
def go_to_piano(browser):
    """
    Inicializa la página del piano.
    Pide la fixture "browser" como parámetro y Pytest la inyecta automáticamente.
    """
    # Se crea una instancia del Page Object y se guarda para usarla en los siguientes pasos
    browser.piano_page = PianoPage(browser)


@when('el usuario toca una nueva melodía')
def play_new_melody(browser):
    """
    Este paso permite al usuario tocar una nueva melodía.
    """
    browser.piano_page.tocar_nueva_melodia()


@when(parsers.parse('el usuario toca {veces:d} vez/veces la melodía de "Estrellita"'))
def play_estrellita(browser, veces):
    """
    Este paso ahora captura el número de la frase y lo pasa como parámetro.
    - {veces:d} le dice a pytest-bdd que espere un número entero (dígito).
    - La función ahora recibe el parámetro "veces".
    """
    for _ in range(veces):
        browser.piano_page.tocar_melodia_estrellita()


@then('la secuencia de notas se completa sin errores')
def check_completion(browser):
    """
    Verifica el resultado. Si los pasos anteriores no fallaron, la prueba es exitosa.
    """
    print("Melodía completada exitosamente.")
    time.sleep(3) # Pausa final para observar el resultado
    pass