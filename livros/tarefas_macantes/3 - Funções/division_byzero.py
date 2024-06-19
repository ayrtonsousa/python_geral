def divisor(n1,n2):
    try:
        print(n1/n2)
    except ZeroDivisionError: 
        print("Não é possível dividir por zero!")


divisor(1,0)