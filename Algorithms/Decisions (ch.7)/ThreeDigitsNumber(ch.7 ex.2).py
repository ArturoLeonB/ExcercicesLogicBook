#Read a number and determine if have three digits
def three_digits(num):
    if 1000 > num and num > 99 or -1000 < num and num < -99 :
        print ("Have 3 digits")
    else:
        print ("Have not 3 digits")
        

three_digits(4567)