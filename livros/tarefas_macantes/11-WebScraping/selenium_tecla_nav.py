from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'geckodriver\\geckodriver.exe')
browser.get('https://www.globo.com/')
browser.get('https://globoesporte.globo.com/')

#Botões do navegador
browser.back()    # volta
browser.forward() # avança
browser.refresh() # atualiza
browser.quit()    # fechar

