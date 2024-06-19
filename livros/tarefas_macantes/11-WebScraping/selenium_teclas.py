from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'geckodriver\\geckodriver.exe')
browser.get('https://www.globo.com/')

#Realiza impressão de teclas na página do navegador
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
#htmlElem.send_keys(Keys.HOME)