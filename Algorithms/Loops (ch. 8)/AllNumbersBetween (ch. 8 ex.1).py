 # Read an integer number and show all pair between.
def pair_list(num):
    Aux = 2
    if num > 0:
        for i in range (Aux, num+1, 2):
            print (i)
    if num <= 0:
        for i in range (Aux, num-1, -2):
            print (f"{i},", end="")

pair_list(-9)