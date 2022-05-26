import requests

#exemplo para encontrar falha
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    print(res.raise_for_status())
except Exception as exc:
    print('Ocorreu um problema: %s' % (exc))
