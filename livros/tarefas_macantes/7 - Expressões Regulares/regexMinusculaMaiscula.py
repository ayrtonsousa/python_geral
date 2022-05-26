import re

#busca palabra indiferente de ser maiscula ou minuscula
robocop = re.compile(r'robocop',re.I)
print(robocop.search('ROBOCOP is part man, part machine, all cop').group())

robocop = re.compile(r'ROBOCOP',re.I)
print(robocop.search('robocop is part man, part machine, all cop').group())