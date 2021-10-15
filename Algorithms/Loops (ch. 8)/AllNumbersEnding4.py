#Read two numbers and show all number ending in 4 between their.

def allNumbersEnding4(num1, num2):
    if num1 > num2:
        for i in range (num2, num1):
            if i % 10 == 4:
                print (i, end=", ")
    if num1 < num2:
        for i in range(num1, num2):
            if i % 10 == 4:
                print (i, end=", ")
    if num1 == num2:
        print ("same number")

allNumbersEnding4(2, 56)