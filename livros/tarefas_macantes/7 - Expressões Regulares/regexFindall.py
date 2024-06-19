import re

#retorna lista com strings encontradas
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell 415-555-9998 Work: 212-555-0000')
print(mo)

#no caso de houver grupos para filtrar
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Cell 415-555-9998 Work: 212-555-0000')
print(mo)
