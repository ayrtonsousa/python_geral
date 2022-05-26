from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'geckodriver\\geckodriver.exe')
browser.get('https://cursos.alura.com.br/loginForm')

#Preenche dados e faz o submit

#emailElem = browser.find_element_by_xpath("//input[@type='email']") #busca por elemento e atributo especifico
emailElem = browser.find_element_by_id("login-email")
emailElem.send_keys('ayrton.sousa@hotmail.com')

pwdElem = browser.find_element_by_id("password")
pwdElem.send_keys('@alura2766')

pwdElem.submit()
