import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def bater_ponto_f(url, username, password):
    print("Iniciando o script...")

    # Configuração do WebDriver do Firefox
    firefox_options = Options()
    firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  
    firefox_options.add_argument(r"--profile")
    firefox_options.add_argument(r"C:\Users\est.07545996984\AppData\Roaming\Mozilla\Firefox\Profiles\z8in9zny.teste_ponto")

    # Configuração de localização simulada
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    firefox_capabilities['moz:firefoxOptions'] = {
        'prefs': {
            'geo.prompt.testing': True,
            'geo.prompt.testing.allow': True,
            'geo.provider.use_corelocation': False,
            'geo.provider.use_gpsd': False,
            'geo.provider.use_wif': False,
            'geo.provider.use_mls': False,
            'geo.wifi.uri': 'data:application/json,{"location": {"lat": -25.4372, "lng": -49.2698}, "accuracy": 100.0}'
        }
    }

    # Configuração do GeckoDriver
    service = Service(r'C:\geckodriver\geckodriver.exe')  
    driver = webdriver.Firefox(service=service, options=firefox_options)

    print("Driver do Firefox iniciado.")

    # Abre o site de registro de ponto
    driver.get(url)
    print(f"URL {url} acessada.")
    
    # Espera a página carregar
    time.sleep(2)  

    # Insere o nome de usuário
    try:
        username_field = driver.find_element(By.ID, "UserName") 
        username_field.send_keys(username)
        print("Nome de usuário inserido.")
    except Exception as e:
        print(f"Erro ao inserir o nome de usuário: {e}")

    # Insere a senha
    try:
        password_field = driver.find_element(By.ID, "Password") 
        password_field.send_keys(password)
        print("Senha inserida.")
    except Exception as e:
        print(f"Erro ao inserir a senha: {e}")

    # Clica no botão de login
    try:
        login_button = driver.find_element(By.ID, "LoginButton")  
        login_button.click()
        print("Botão de login clicado.")
        time.sleep(2) 
    except Exception as e:
        print(f"Erro ao clicar no botão de login: {e}")
    
    # Localiza e clica no botão para abrir a aba do ponto
    try:
        ponto_button = driver.find_element(By.ID, "ctl00_TopBar_ctl00_RegistrarPontoHyperLink")  
        ponto_button.click()
        print("Botão de abrir a aba do ponto clicado.")
    except Exception as e:
        print(f"Erro ao clicar no botão deabrir a aba do ponto: {e}")

    # Espera alguns segundos para garantir que a geolocalização foi realizada
    time.sleep(4)

    # Localiza e clica no botão de bater ponto
    try:
        ponto_button = driver.find_element(By.ID, "BtnRegistr")  
        ponto_button.click()
        print("Botão de bater ponto clicado.")
    except Exception as e:
        print(f"Erro ao clicar no botão de bater ponto: {e}")
    
    # Espera alguns segundos para garantir que o ponto foi registrado
    time.sleep(5)
    
    # Fecha o navegador após a operação
    driver.quit()
    print("Driver do Firefox fechado.")

# Exemplo de uso
url = 'https://celepar.bennercloud.com.br/RH/rh/e/Colaborador/Home/home.aspx?i=HOME&m=QUI_HOME'
username = 'est.bmesquita' 
password = 'Ma009bruno' 
bater_ponto_f(url, username, password)
