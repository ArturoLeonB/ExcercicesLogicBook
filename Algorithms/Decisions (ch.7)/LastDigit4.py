#Read an integer number and determine if it is a number that ends in 4
def Ult_Dig_4(num):
    x = num % 10
    print (x)
    if x == 4 :
        print ("Last digit is 4")
    if x != 4:
        print ("Last digit is not 4")
        
