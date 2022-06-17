# slicing
l =[10,20,30,40]
# print(l[:3]) 
# print(l[1:]) 

# [a:b:c] especificando pulo
s = 'bicycle'
# print(s[::3])
# print(s[::-1])
# print(s[::-2])

# 2.11
invoice = '''
0.....6.............20.........30..33.............50
1909  Caixa de Leite   R$ 2,50     3    R$ 7,50  
2300  Pão Francês      R$ 0,50     6    R$ 3,00
'''
ID = slice(0,6)
DESCRIPTION = slice(6,20)
UNIT_PRICE = slice(20,30)
QUANTITY = slice(30,33)
ITEM_TOTAL = slice(33,50)

line_items = invoice.split('\n')[2:]


for item in line_items:
    print(item[ID], item[DESCRIPTION], item[QUANTITY],  item[UNIT_PRICE], item[ITEM_TOTAL])