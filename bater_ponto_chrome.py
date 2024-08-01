import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def bater_ponto_c(url, username, password):
    print("Iniciando o script...")

    # Configuração do WebDriver do Chrome
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  
    
      # Configuração do ChromeDriver
    service = Service(r'C:\chromedriver\chromedriver.exe')
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        print("Driver do Chrome iniciado.")
    except Exception as e:
        print(f"Erro ao iniciar o ChromeDriver: {e}")
        return
    
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
        print(f"Erro ao clicar no botão de abrir a aba do ponto: {e}")

    # Espera alguns segundos para garantir que a geolocalização foi realizada
    time.sleep(4)

    # Localiza e clica no botão de bater ponto
    try:
        ponto_button = driver.find_element(By.ID, "BtnRegistrar")  
        ponto_button.click()
        print("Botão de bater ponto clicado.")
    except Exception as e:
        print(f"Erro ao clicar no botão de bater ponto: {e}")
    
    # Espera alguns segundos para garantir que o ponto foi registrado
    time.sleep(5)
    
    # Fecha o navegador após a operação
    driver.quit()
    print("Driver do Chrome fechado.")

# Exemplo de uso
url = 'https://celepar.bennercloud.com.br/RH/rh/e/Colaborador/Home/home.aspx?i=HOME&m=QUI_HOME'
username = 'est.bmesquita'  # Substitua pelo seu nome de usuário
password = 'Ma009bruno'  # Substitua pela sua senha
bater_ponto_c(url, username, password)
