#1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído
def numbers_between_givennumber(num):
    x = 1
    if num > 0:
        while x <= num:
            print (x)
            x = x + 1
    if num <= 0:
        while x >= num:
            print (x)
            x = x - 1
numbers_between_givennumber(9)