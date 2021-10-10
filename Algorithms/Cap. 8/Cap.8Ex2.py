# Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.
def pair_list(num):
    Aux = 2
    if num > 0:
        for i in range (Aux, num+1, 2):
            print (i)
    if num <= 0:
        for i in range (Aux, num-1, -2):
            print (f"{i},", end="")

pair_list(-9)