#Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.
def suma_guarismo():
    num = int(input())
    suma = (num % 10) + (num // 10)
    print (suma)
    
    
suma_guarismo()