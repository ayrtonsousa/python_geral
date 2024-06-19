from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'geckodriver\\geckodriver.exe')
browser.get('https://inventwithpython.com')

#Busca texto em links e clica
linkElem = browser.find_element_by_link_text('Invent with Python Blog')
linkElem.click()