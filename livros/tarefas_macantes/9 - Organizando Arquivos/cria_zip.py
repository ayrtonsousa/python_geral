import zipfile

#Cria Zip
newZip = zipfile.ZipFile('new.zip','w')
newZip.write('bacon.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()