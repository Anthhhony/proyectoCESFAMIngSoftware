from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configurar Selenium con Chrome
options = Options()
options.add_argument("--start-maximized")
service = Service(executable_path="ruta/a/chromedriver")  # Cambia la ruta según tu sistema
driver = webdriver.Chrome(service=service, options=options)

# Prueba de login
def test_login():
    driver.get("http://127.0.0.1:8000/buscar-usuario/")  # Ajusta según la URL de login
    # Llenar formulario
    driver.find_element(By.NAME, "rut").send_keys("12345678-9")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Ingresar')]").click()
    time.sleep(2)
    # Validar redirección y contenido
    assert "menu.html" in driver.current_url
    assert "Menú Principal" in driver.page_source  # Ajusta según el contenido real
    print("Prueba de login exitosa.")

test_login()
driver.quit()
