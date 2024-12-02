from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o WebDriver (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Chrome()

try:
    # Acessar o Google
    driver.get("https://www.google.com")
    print("Acessou o Google")

    # Localizar o campo de busca
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")  # Realizar busca
    search_box.send_keys(Keys.RETURN)

    # Esperar os resultados carregarem
    time.sleep(2)

    # Verificar se o título da página contém o termo buscado
    assert "Selenium Python" in driver.title
    print("Teste de busca no Google: PASSED")
finally:
    # Fechar o navegador
    driver.quit()
