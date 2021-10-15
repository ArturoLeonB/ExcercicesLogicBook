#Read a number and show all divisors between 1 and num.

def all_submultiples(num):
    for i in range(1, num+1):
        if (num % i) == 0:
            print (i, end=",")

all_submultiples(12)
