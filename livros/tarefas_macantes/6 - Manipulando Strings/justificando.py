def printPicnic(itemsDict,leftWidth,rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches':4,'apples':3,'cups':4,'cookies':30}

printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)