#Read a number and determine if their two digits are pair
def two_digits_pair(num):
    if (num % 10) % 2 == 0 and (num // 10) % 2 == 0:
        print ("Two digits are pair")
    else:
        print ("At least one digit is pair")
        
        
two_digits_pair(21)

    
    
