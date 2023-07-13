from selenium import webdriver
from webdriverdownloader import ChromeDriverDownloader
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

# Un pequeño ejemplo de como se podria parametrizar usando variables de entonrno
url= os.getenv("URL")
term = os.getenv("SEARCH_TERM")


# Definimos el test como una funcion, para mas reusabilidad, organizacion y facil mantenimiento.
def test_search(url, term):
    downloader = ChromeDriverDownloader()
    downloader.download_and_install()
    driver = webdriver.Chrome()

    driver.get(url)

    # Verificamos que estamos en la pagina de google
    try:
        assert driver.title == "Google"
    except AssertionError as e:
        print("Error: Element not found..", e)

    driver.maximize_window()

    # Usamos el WebDriverWait para hacer esperar de manera implicita la aparicion del elemento, en vez de usar sleeps
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

    search_input.send_keys(term)

    # Usamos la tecla Enter para evitar problemas con el element name btnK y selenium
    search_input.send_keys(Keys.RETURN)

    # Buscamos el primer resultado que contenga la palabra Wikipedia
    search_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Wikipedia")))
    
    search_result.click()

    # Verificamos que estamos en la pagina de Wikipedia. En esta ocasion esta validando wikipedia en español, porque asi se abre en el browser.
    try:
        assert driver.title == "Wikipedia, la enciclopedia libre"
    except AssertionError as e:
        print("Error: Element not found..", e)

    driver.quit()

test_search(url, term)
