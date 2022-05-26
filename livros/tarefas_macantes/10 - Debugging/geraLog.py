import traceback

try:
    raise Exception('Isso e uma mensagem de erro')

except:
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

