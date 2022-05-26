from selenium import webdriver

#Abre navegador firefox com selenium e geckodriver
browser = webdriver.Firefox(executable_path=r'geckodriver\\geckodriver.exe')
print(type(browser))
browser.get('https://inventwithpython.com')

#Busca elemento que tenha o nome da classe
try:
    elem = browser.find_element_by_class_name('jumbotron')
    print('Encontrado <%s> elemento com o nome de classe!' % (elem.tag_name))
except:
    print('Não foi possível encontrar um elemento com esse nome')