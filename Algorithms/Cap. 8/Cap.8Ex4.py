#4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.
def AllIntBetween(num1, num2):
    if num1 > num2:
        for i in range (num2, num1):
            print (i, end=", ")
    if num1 < num2:
        for i in range(num1, num2):
            print (i, end=", ")
    if num1 == num2: 
        print ("same number")
AllIntBetween(-8, 2)

