"""
Testes End-to-End com Selenium para a Gerenciadora de Estacionamentos.

Este script automatiza a interação do usuário com o front-end hospedado,
verificando os principais fluxos da aplicação.
"""

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- Configuração do Teste ---
# URL do seu site hospedado no Netlify
APP_URL = "https://gerenciadoradeestacionamento.netlify.app/"

@pytest.fixture(scope="module")
def driver():
    """
    Fixture do Pytest que configura e inicializa o WebDriver do Chrome.
    Esta função é executada uma vez antes de todos os testes do módulo.
    """
    print("INFO: Configurando o WebDriver do Chrome...")
    service = ChromeService(ChromeDriverManager().install())
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(20) # Aumentar o tempo de espera implícito geral
    
    print("INFO: WebDriver configurado. A iniciar os testes.")
    yield driver
    
    print("INFO: Testes concluídos. A fechar o WebDriver.")
    driver.quit()

def test_full_workflow(driver):
    """
    Testa o fluxo completo da aplicação:
    1. Login
    2. Criação de um Estacionamento
    3. Criação de um Acesso
    4. Geração de um Relatório
    5. Exclusão do Acesso e do Estacionamento
    """
    
    # --- 1. Login ---
    print("TEST: A aceder à página de login...")
    driver.get(APP_URL)
    assert "Gerenciadora de Estacionamentos" in driver.title

    driver.find_element(By.CSS_SELECTOR, 'input[type="email"]').send_keys("test@example.com")
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print("TEST: Login efetuado com sucesso.")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "page-home"))
    )
    
    # --- 2. Criação de Estacionamento ---
    print("TEST: A navegar para a criação de estacionamento...")
    driver.find_element(By.CSS_SELECTOR, 'a[href="#estacionamentos"]').click()
    
    print("INFO: A aguardar até 45 segundos para a API do Render acordar...")
    time.sleep(45)
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='estacionamentos-table-body']//tr"))
    )

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar um Estacionamento')]"))
    )
    add_button.click()
    
    print("TEST: A preencher o formulário de novo estacionamento...")
    nome_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "estacionamento-nome"))
    )
    nome_input.send_keys("Estacionamento Teste Final")
    
    driver.find_element(By.ID, "estacionamento-cnpj").send_keys("11.222.333/0001-55")
    driver.find_element(By.ID, "estacionamento-valorFracao").send_keys("5.00")
    driver.find_element(By.ID, "estacionamento-valorHoraCheia").send_keys("12.00")
    driver.find_element(By.ID, "estacionamento-valorDiaria").send_keys("45.00")
    driver.find_element(By.ID, "estacionamento-valorMensalista").send_keys("250.00")
    driver.find_element(By.ID, "estacionamento-valorEvento").send_keys("60.00")
    driver.find_element(By.ID, "estacionamento-valorNoturno").send_keys("30.00")
    driver.find_element(By.ID, "estacionamento-horarioNoturnoInicio").send_keys("20:00")
    driver.find_element(By.ID, "estacionamento-horarioNoturnoFim").send_keys("06:00")
    driver.find_element(By.ID, "estacionamento-capacidade").send_keys("80")
    driver.find_element(By.ID, "estacionamento-percentualRepasse").send_keys("15")
    
    driver.find_element(By.XPATH, "//form[@id='estacionamento-form']//button[text()='Salvar']").click()
    print("TEST: Estacionamento salvo.")
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Estacionamento Teste Final')]"))
    )
    print("SUCCESS: Estacionamento criado e verificado na tabela.")
    
    # --- 3. Criação de Acesso ---
    print("TEST: A navegar para a criação de acesso...")
    driver.find_element(By.CSS_SELECTOR, 'a[href="#acessos"]').click()
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='acessos-table-body']//tr"))
    )
    
    add_acesso_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar um Acesso')]"))
    )
    add_acesso_button.click()
    
    print("TEST: A preencher o formulário de novo acesso...")
    acesso_placa_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "acesso-placa"))
    )
    acesso_placa_input.send_keys("TEST-999")
    
    estacionamento_select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "acesso-estacionamento-id"))
    )
    select = Select(estacionamento_select_element)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//option[text()='Estacionamento Teste Final']"))
    )
    select.select_by_visible_text("Estacionamento Teste Final")
    print("TEST: Estacionamento selecionado no dropdown.")
    
    driver.execute_script("document.getElementById('acesso-data-entrada').value = '2025-07-12'")
    driver.find_element(By.ID, "acesso-hora-entrada").send_keys("10:00")
    driver.execute_script("document.getElementById('acesso-data-saida').value = '2025-07-12'")
    driver.find_element(By.ID, "acesso-hora-saida").send_keys("11:30")
    
    driver.find_element(By.XPATH, "//form[@id='acesso-form']//button[text()='Salvar']").click()
    print("TEST: Acesso salvo.")
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'TEST-999')]"))
    )
    print("SUCCESS: Acesso criado e verificado na tabela.")
    
    # --- 4. Geração de Relatório ---
    print("TEST: A navegar para a geração de relatório...")
    driver.find_element(By.CSS_SELECTOR, 'a[href="#relatorios"]').click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "relatorio-form"))
    )
    driver.execute_script("document.getElementById('relatorio-data-inicio').value = '2025-07-12'")
    driver.execute_script("document.getElementById('relatorio-data-fim').value = '2025-07-13'")
    driver.find_element(By.XPATH, "//form[@id='relatorio-form']//button[text()='Gerar']").click()
    
    resultado_faturamento = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "relatorio-resultado"))
    )
    assert resultado_faturamento.is_displayed()
    print("SUCCESS: Relatório gerado com sucesso.")
    
    # --- 5. Limpeza (Exclusão) ---
    print("TEST: A iniciar a limpeza dos dados de teste...")
    
    driver.find_element(By.CSS_SELECTOR, 'a[href="#acessos"]').click()
    delete_button_acesso = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[text()='TEST-999']/following-sibling::td/button[text()='Deletar']"))
    )
    delete_button_acesso.click()
    
    driver.find_element(By.ID, "delete-confirm-button").click()
    
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//td[contains(text(), 'TEST-999')]"))
    )
    print("SUCCESS: Acesso de teste excluído.")
    
    driver.find_element(By.CSS_SELECTOR, 'a[href="#estacionamentos"]').click()
    delete_button_est = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[text()='Estacionamento Teste Final']/following-sibling::td/button[text()='Deletar']"))
    )
    delete_button_est.click()
    
    driver.find_element(By.ID, "delete-confirm-button").click()
    
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//td[contains(text(), 'Estacionamento Teste Final')]"))
    )
    print("SUCCESS: Estacionamento de teste excluído.")
    print("--- Teste de fluxo completo concluído com sucesso! ---")
