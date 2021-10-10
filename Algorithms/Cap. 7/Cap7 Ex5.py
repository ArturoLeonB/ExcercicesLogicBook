#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
def dos_dig():
    num = int(input())
    if (num % 10) % 2 == 0 and (num // 10) % 2 == 0:
        print (num)
    else:
        print ("Existe al menos un dígito impar")
        
        
dos_dig()

    
    
