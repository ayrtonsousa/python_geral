import re

#substituir palavra
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#substituindo somente parte da palavra
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
